class Barco:
    def __init__(self, nombre, posicionX, posicionY, velocidad, rumbo, numeroMunicion):
        self.nombre = nombre
        self.posicionX = posicionX
        self.posicionY = posicionY
        self.velocidad = velocidad  # entre 0 y 20 km/h
        self.rumbo = rumbo          # entre 1 y 359 grados
        self.numeroMunicion = numeroMunicion

    def __str__(self):
        return (f"Barco {self.nombre}: Pos({self.posicionX},{self.posicionY}), "
                f"Velocidad={self.velocidad} km/h, Rumbo={self.rumbo}°, "
                f"Munición={self.numeroMunicion}")

    def disparar(self):
        if self.numeroMunicion > 0:
            self.numeroMunicion -= 1
            print("💥 El barco ha disparado")
        else:
            print("⚠️ No queda munición")

    def setVelocidad(self, nueva_velocidad):
        if 0 <= nueva_velocidad <= 20:
            self.velocidad = nueva_velocidad
        else:
            print("⚠️ Velocidad fuera de rango (0-20 km/h)")

    def setRumbo(self, nuevo_rumbo):
        if 1 <= nuevo_rumbo <= 359:
            self.rumbo = nuevo_rumbo
        else:
            print("⚠️ Rumbo fuera de rango (1-359 grados)")


# Crear 3 barcos y probar métodos
barco1 = Barco("Titanic", 0, 0, 10, 90, 5)
barco2 = Barco("Bismarck", 5, 10, 15, 180, 3)
barco3 = Barco("Yamato", -3, 7, 20, 270, 10)

for barco in [barco1, barco2, barco3]:
    print(barco)
    barco.disparar()
    barco.setVelocidad(12)
    barco.setRumbo(45)
    print(barco)
    print("-" * 40)
