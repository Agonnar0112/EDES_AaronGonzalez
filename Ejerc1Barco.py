import tkinter as tk
from tkinter import ttk
import pygame

# Inicializar pygame para sonido
pygame.mixer.init()
pygame.mixer.music.load("fondo.mp3")  # música de fondo
pygame.mixer.music.play(-1)           # loop infinito
sonido_disparo = pygame.mixer.Sound("disparo.wav")

# Lista de barcos
barcos = []

def crear_barco():
    nombre = f"Barco{len(barcos)+1}"
    nuevo = Barco(nombre, 50, 50, 5, 90, 3)
    barcos.append(nuevo)
    actualizar_selector()

def actualizar_selector():
    selector["values"] = [b.nombre for b in barcos]

def disparar():
    seleccionado = selector.get()
    for b in barcos:
        if b.nombre == seleccionado:
            b.disparar()
            sonido_disparo.play()

# Ventana principal
root = tk.Tk()
root.title("Batalla Naval")

selector = ttk.Combobox(root, state="readonly")
selector.pack()

btn_crear = tk.Button(root, text="Crear Barco", command=crear_barco)
btn_crear.pack()

btn_disparar = tk.Button(root, text="Disparar", command=disparar)
btn_disparar.pack()

root.mainloop()
