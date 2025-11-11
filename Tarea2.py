import tkinter as tk
from tkinter import messagebox

# Función para convertir Celsius a Fahrenheit
def convertir_temperatura():
    try:
        celsius = float(entry_temp.get())
        fahrenheit = (celsius * 9 / 5) + 32
        resultado.config(text=f"{celsius}°C = {fahrenheit:.2f}°F")
    except ValueError:
        messagebox.showerror("Error", "Introduce un número válido")

# Función para mostrar tabla de multiplicar
def mostrar_tabla():
    try:
        numero = int(entry_tabla.get())
        tabla = ""
        for i in range(1, 11):
            tabla += f"{numero} x {i} = {numero * i}\n"
        resultado.config(text=tabla)
    except ValueError:
        messagebox.showerror("Error", "Introduce un número entero")

# Función para salir
def salir():
    ventana.destroy()

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Menú de Opciones")
ventana.geometry("400x400")

# Etiqueta de instrucciones
instrucciones = tk.Label(ventana, text="Selecciona una opción:", font=("Arial", 14))
instrucciones.pack(pady=10)

# Entrada para temperatura
entry_temp = tk.Entry(ventana)
btn_temp = tk.Button(ventana, text="1) Conversión de temperatura", command=lambda: entry_temp.pack())
btn_convertir = tk.Button(ventana, text="Convertir", command=convertir_temperatura)

# Entrada para tabla
entry_tabla = tk.Entry(ventana)
btn_tabla = tk.Button(ventana, text="2) Tabla de multiplicar", command=lambda: entry_tabla.pack())
btn_mostrar_tabla = tk.Button(ventana, text="Mostrar tabla", command=mostrar_tabla)

# Botón salir
btn_salir = tk.Button(ventana, text="3) Salir", command=salir)

# Resultado
resultado = tk.Label(ventana, text="", font=("Courier", 12), justify="left")

# Mostrar botones
btn_temp.pack(pady=5)
btn_convertir.pack(pady=5)
btn_tabla.pack(pady=5)
btn_mostrar_tabla.pack(pady=5)
btn_salir.pack(pady=20)
resultado.pack(pady=10)

# Ejecutar ventana
ventana.mainloop()
