import tkinter as tk
from tkinter import messagebox
import random

# Reutilizamos las clases lógicas básicas, pero adaptadas para GUI
class NaveVisual:
    def __init__(self, canvas, nombre, tipo, x, y, color):
        self.canvas = canvas
        self.nombre = nombre
        self.tipo = tipo
        self.vida = 100
        self.velocidad = 0
        self.color = color
        
        # Representación gráfica (un rectángulo y texto)
        self.id_shape = canvas.create_rectangle(x, y, x+60, y+30, fill=color, outline="white")
        self.id_text = canvas.create_text(x+30, y-10, text=nombre, fill="white", font=("Arial", 8))
        
        # Vectores de movimiento
        self.dx = 0
        self.dy = 0

    def mover(self):
        # Mueve la nave en el canvas si tiene velocidad
        if self.velocidad > 0:
            self.canvas.move(self.id_shape, self.dx, self.dy)
            self.canvas.move(self.id_text, self.dx, self.dy)
            
            # Rebote básico en los bordes para mantenerlos en pantalla
            pos = self.canvas.coords(self.id_shape)
            if pos[2] >= 600 or pos[0] <= 0: self.dx = -self.dx
            if pos[3] >= 400 or pos[1] <= 0: self.dy = -self.dy

    def cambiar_rumbo(self):
        # Simula cambio de rumbo aleatorio
        self.velocidad = random.randint(1, 5)
        self.dx = random.choice([-1, 1]) * self.velocidad
        self.dy = random.choice([-1, 1]) * (self.velocidad * 0.5)

    def recibir_danio_visual(self, cantidad):
        self.vida -= cantidad
        if self.vida < 0: self.vida = 0
        # Cambiar color si está muy dañado
        if self.vida < 30:
            self.canvas.itemconfig(self.id_shape, fill="red")
        elif self.vida < 70:
            self.canvas.itemconfig(self.id_shape, fill="orange")

# --- CLASE PRINCIPAL DE LA APP ---
class SimuladorNavalGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador Naval - Flota del Atlántico")
        self.root.geometry("800x500")

        # 1. Configurar el Canvas (Mar)
        self.canvas = tk.Canvas(root, bg="#1a3b5c", width=600, height=400)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # 2. Panel de Control (Derecha) [cite: 31]
        self.panel = tk.Frame(root, bg="#ccc", width=200)
        self.panel.pack(side=tk.RIGHT, fill=tk.Y)

        tk.Label(self.panel, text="Panel de Control", font=("Arial", 12, "bold"), bg="#ccc").pack(pady=10)

        # Labels de información
        self.lbl_nombre = tk.Label(self.panel, text="Nave: Ninguna", bg="#ccc")
        self.lbl_nombre.pack()
        self.lbl_vida = tk.Label(self.panel, text="Vida: --", bg="#ccc")
        self.lbl_vida.pack()
        self.lbl_estado = tk.Label(self.panel, text="Estado: --", bg="#ccc")
        self.lbl_estado.pack()

        tk.Frame(self.panel, height=2, bd=1, relief=tk.SUNKEN).pack(fill=tk.X, padx=5, pady=10)

        # Botones de Acción
        self.btn_mover = tk.Button(self.panel, text="Cambiar Rumbo/Velocidad", command=self.accion_mover, state=tk.DISABLED)
        self.btn_mover.pack(pady=5, fill=tk.X, padx=10)

        self.btn_atacar = tk.Button(self.panel, text="Simular Daño Recibido", command=self.accion_daniar, state=tk.DISABLED, bg="#ffdddd")
        self.btn_atacar.pack(pady=5, fill=tk.X, padx=10)

        # 3. Crear Flota Visual
        self.naves = []
        self.crear_naves()

        # Variable para la nave seleccionada [cite: 31]
        self.nave_seleccionada = None

        # Bind de eventos del ratón para selección
        self.canvas.bind("<Button-1>", self.seleccionar_nave)

        # 4. Iniciar bucle de animación [cite: 30]
        self.animar()

    def crear_naves(self):
        # Instanciar naves gráficas
        f = NaveVisual(self.canvas, "Fragata F100", "Fragata", 50, 50, "#555555")
        c = NaveVisual(self.canvas, "Corbeta C20", "Corbeta", 200, 100, "#777777")
        s = NaveVisual(self.canvas, "Submarino S80", "Submarino", 100, 250, "#222222")
        self.naves = [f, c, s]

    def seleccionar_nave(self, event):
        # Detectar clic sobre una nave
        x, y = event.x, event.y
        items = self.canvas.find_overlapping(x, y, x+1, y+1)
        
        if items:
            # Buscar cuál nave corresponde al ID clicado
            for nave in self.naves:
                if nave.id_shape in items or nave.id_text in items:
                    self.nave_seleccionada = nave
                    self.actualizar_panel()
                    self.btn_mover.config(state=tk.NORMAL)
                    self.btn_atacar.config(state=tk.NORMAL)
                    # Feedback visual de selección (borde amarillo)
                    self.canvas.itemconfig(nave.id_shape, outline="yellow", width=2)
                else:
                    self.canvas.itemconfig(nave.id_shape, outline="white", width=1)

    def actualizar_panel(self):
        if self.nave_seleccionada:
            n = self.nave_seleccionada
            self.lbl_nombre.config(text=f"Nave: {n.nombre}\nTipo: {n.tipo}")
            self.lbl_vida.config(text=f"Vida: {n.vida}%")
            estado = "Operativa" if n.vida > 0 else "Destruida"
            self.lbl_estado.config(text=f"Estado: {estado}", fg="green" if n.vida > 0 else "red")

    def accion_mover(self):
        if self.nave_seleccionada and self.nave_seleccionada.vida > 0:
            self.nave_seleccionada.cambiar_rumbo()
            print(f"{self.nave_seleccionada.nombre} cambia de rumbo.")

    def accion_daniar(self):
        if self.nave_seleccionada and self.nave_seleccionada.vida > 0:
            damage = random.randint(10, 25)
            self.nave_seleccionada.recibir_danio_visual(damage)
            self.actualizar_panel()
            print(f"{self.nave_seleccionada.nombre} recibe daño.")

    def animar(self):
        for nave in self.naves:
            if nave.vida > 0: # Solo se mueven si están vivas
                nave.mover()
        self.root.after(50, self.animar) # Loop cada 50ms

if __name__ == "__main__":
    ventana = tk.Tk()
    app = SimuladorNavalGUI(ventana)
    ventana.mainloop()