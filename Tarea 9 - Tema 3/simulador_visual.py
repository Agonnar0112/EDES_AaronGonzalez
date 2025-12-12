import tkinter as tk
from modelo_espacial import * # Importa tus clases del ejercicio anterior

class SimuladorVisual:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador Espacial - Ejercicio 9")
        self.root.geometry("800x600")

        # Configuración del Canvas (Espacio) [cite: 158]
        self.canvas = tk.Canvas(root, bg="#0b0b1a", width=600, height=600)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Panel Lateral [cite: 162]
        self.panel = tk.Frame(root, bg="gray", width=200)
        self.panel.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.lbl_info = tk.Label(self.panel, text="Selecciona un objeto", wraplength=180)
        self.lbl_info.pack(pady=20)

        # Botones de control [cite: 163]
        self.btn_avanzar = tk.Button(self.panel, text="Avanzar Tiempo (1 paso)", command=self.avanzar_un_paso)
        self.btn_avanzar.pack(pady=5)
        
        self.btn_animar = tk.Button(self.panel, text="Iniciar Animación", command=self.toggle_animacion)
        self.btn_animar.pack(pady=5)

        self.animando = False
        
        # Crear objetos para la simulación visual
        self.crear_objetos_simulacion()
        self.dibujar_todo()

    def crear_objetos_simulacion(self):
        self.objetos = []
        
        # Planeta central (estático visualmente para referencia, o con poca velocidad)
        tierra = Planeta("Tierra", 300, 300, 0, 0, 100, "Solar", 50, 1, True)
        
        # Satélite orbitando (con velocidad para moverse)
        luna = SateliteNatural("Luna", 450, 300, 0, 2, 20, "Solar", "Tierra", 150)
        
        # Nave humana
        iss = SateliteArtificial("ISS", 350, 350, -1, 1, "ESA/NASA", "Int", "Tierra", "Lab")

        self.objetos.append({"obj": tierra, "color": "blue", "size": 30})
        self.objetos.append({"obj": luna, "color": "white", "size": 10})
        self.objetos.append({"obj": iss, "color": "red", "size": 5})

    def dibujar_todo(self):
        self.canvas.delete("all") # Limpiar pantalla
        
        for item in self.objetos:
            obj = item["obj"]
            r = item["size"]
            
            # Dibujar círculo o cuadrado
            # Nota: Usamos las coordenadas del objeto x,y para pintar
            tag = obj.nombre
            if isinstance(obj, EstructuraArtificial):
                # Representar estructuras como cuadraditos [cite: 161]
                self.canvas.create_rectangle(obj.x-r, obj.y-r, obj.x+r, obj.y+r, fill=item["color"], tags=tag)
            else:
                # Representar naturales como círculos [cite: 159]
                self.canvas.create_oval(obj.x-r, obj.y-r, obj.x+r, obj.y+r, fill=item["color"], tags=tag)
            
            # Texto del nombre
            self.canvas.create_text(obj.x, obj.y+r+10, text=obj.nombre, fill="white", font=("Arial", 8))

        # Evento de clic para seleccionar [cite: 166]
        self.canvas.bind("<Button-1>", self.seleccionar_objeto)

    def avanzar_un_paso(self):
        # Lógica de "vibe coding": movemos objetos y redibujamos [cite: 168]
        for item in self.objetos:
            obj = item["obj"]
            obj.avanzar_tiempo() 
            
            # Rebote simple para que no se salgan de pantalla (opcional)
            if obj.x > 600 or obj.x < 0: obj.vx *= -1
            if obj.y > 600 or obj.y < 0: obj.vy *= -1
            
        self.dibujar_todo()

    def toggle_animacion(self):
        self.animando = not self.animando
        if self.animando:
            self.btn_animar.config(text="Parar Animación")
            self.loop_animacion()
        else:
            self.btn_animar.config(text="Iniciar Animación")

    def loop_animacion(self):
        if self.animando:
            self.avanzar_un_paso()
            self.root.after(50, self.loop_animacion) # 50ms refresh rate

    def seleccionar_objeto(self, event):
        # Detectar qué objeto está cerca del click
        x, y = event.x, event.y
        for item in self.objetos:
            obj = item["obj"]
            # Detección de colisión simple (caja de 20px)
            if abs(obj.x - x) < 20 and abs(obj.y - y) < 20:
                info = f"Nombre: {obj.nombre}\n"
                info += f"Pos: ({obj.x}, {obj.y})\n"
                info += f"Vel: ({obj.vx}, {obj.vy})\n"
                if isinstance(obj, EstructuraArtificial):
                    info += f"Agencia: {obj.agencia}\n"
                    info += f"Combustible: {obj.motor.cantidad}"
                self.lbl_info.config(text=info)
                return

if __name__ == "__main__":
    ventana = tk.Tk()
    app = SimuladorVisual(ventana)
    ventana.mainloop()