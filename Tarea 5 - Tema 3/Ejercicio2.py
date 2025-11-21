import tkinter as tk
from tkinter import messagebox
import pygame

# -------------------------------
# Clases del Ejercicio 1
# -------------------------------
class Caja:
    def __init__(self, codigo, peso_kg, descripcion_carga, largo, ancho, altura):
        self.codigo = codigo
        self.peso_kg = peso_kg
        self.descripcion_carga = descripcion_carga
        self.largo = largo
        self.ancho = ancho
        self.altura = altura

    def __str__(self):
        return f"Caja {self.codigo}: {self.descripcion_carga}, {self.peso_kg} kg, {self.largo}x{self.ancho}x{self.altura} m"


class Camion:
    def __init__(self, matricula, conductor, capacidad_kg):
        self.matricula = matricula
        self.conductor = conductor
        self.capacidad_kg = capacidad_kg
        self.descripcion_carga = ""
        self.rumbo = 0
        self.velocidad = 0
        self.cajas = []

    def peso_total(self):
        return sum(c.peso_kg for c in self.cajas)

    def add_caja(self, caja):
        if self.peso_total() + caja.peso_kg <= self.capacidad_kg:
            self.cajas.append(caja)
        else:
            messagebox.showwarning("Capacidad excedida", f"No se puede añadir la caja {caja.codigo}, supera la capacidad.")

    def setVelocidad(self, v):
        self.velocidad = v

    def setRumbo(self, r):
        if 1 <= r <= 359:
            self.rumbo = r
        else:
            messagebox.showerror("Error", "El rumbo debe estar entre 1 y 359 grados.")

    def claxon(self):
        pygame.mixer.init()
        try:
            pygame.mixer.music.load("claxon.mp3")  # Debes tener un archivo de sonido llamado claxon.mp3
            pygame.mixer.music.play()
        except:
            messagebox.showinfo("Claxon", "piiiiiii (no se encontró archivo de sonido)")

    def __str__(self):
        return (f"Camión {self.matricula}, Conductor: {self.conductor}, "
                f"Capacidad: {self.capacidad_kg} kg, Rumbo: {self.rumbo}, Velocidad: {self.velocidad}, "
                f"Cajas: {len(self.cajas)}, Peso total: {self.peso_total()} kg")


# -------------------------------
# Interfaz gráfica con Tkinter
# -------------------------------
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Camiones")

        self.camiones = []
        self.camion_activo = None

        # Selector de camión
        self.selector = tk.Listbox(root, height=5)
        self.selector.pack()
        self.selector.bind("<<ListboxSelect>>", self.seleccionar_camion)

        # Botones de acciones
        tk.Button(root, text="Nuevo Camión", command=self.nuevo_camion).pack()
        tk.Button(root, text="Añadir Caja", command=self.nueva_caja).pack()
        tk.Button(root, text="Cambiar Velocidad", command=self.cambiar_velocidad).pack()
        tk.Button(root, text="Cambiar Rumbo", command=self.cambiar_rumbo).pack()
        tk.Button(root, text="Mostrar Info", command=self.mostrar_info).pack()
        tk.Button(root, text="Claxon", command=self.tocar_claxon).pack()

    def actualizar_selector(self):
        self.selector.delete(0, tk.END)
        for c in self.camiones:
            self.selector.insert(tk.END, f"{c.matricula} - {c.conductor}")

    def seleccionar_camion(self, event):
        idx = self.selector.curselection()
        if idx:
            self.camion_activo = self.camiones[idx[0]]

    def nuevo_camion(self):
        matricula = simple_input("Matrícula del camión:")
        conductor = simple_input("Conductor:")
        capacidad = float(simple_input("Capacidad máxima (kg):"))
        c = Camion(matricula, conductor, capacidad)
        self.camiones.append(c)
        self.actualizar_selector()

    def nueva_caja(self):
        if not self.camion_activo:
            messagebox.showerror("Error", "Selecciona un camión primero.")
            return
        codigo = simple_input("Código de la caja:")
        peso = float(simple_input("Peso (kg):"))
        desc = simple_input("Descripción:")
        largo = float(simple_input("Largo (m):"))
        ancho = float(simple_input("Ancho (m):"))
        altura = float(simple_input("Altura (m):"))
        caja = Caja(codigo, peso, desc, largo, ancho, altura)
        self.camion_activo.add_caja(caja)

    def cambiar_velocidad(self):
        if self.camion_activo:
            v = int(simple_input("Nueva velocidad:"))
            self.camion_activo.setVelocidad(v)

    def cambiar_rumbo(self):
        if self.camion_activo:
            r = int(simple_input("Nuevo rumbo (1-359):"))
            self.camion_activo.setRumbo(r)

    def mostrar_info(self):
        if self.camion_activo:
            info = str(self.camion_activo) + "\n\nCajas:\n" + "\n".join(str(c) for c in self.camion_activo.cajas)
            messagebox.showinfo("Información del camión", info)

    def tocar_claxon(self):
        if self.camion_activo:
            self.camion_activo.claxon()


# -------------------------------
# Función auxiliar para pedir datos
# -------------------------------
def simple_input(prompt):
    top = tk.Toplevel()
    top.title(prompt)
    tk.Label(top, text=prompt).pack()
    entry = tk.Entry(top)
    entry.pack()
    result = []

    def ok():
        result.append(entry.get())
        top.destroy()

    tk.Button(top, text="OK", command=ok).pack()
    top.wait_window()
    return result[0] if result else ""


# -------------------------------
# Programa principal
# -------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
