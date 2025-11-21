class Caja:
    def __init__(self, codigo, peso_kg, descripcion_carga, largo, ancho, altura):
        self.codigo = codigo
        self.peso_kg = peso_kg
        self.descripcion_carga = descripcion_carga
        self.largo = largo
        self.ancho = ancho
        self.altura = altura

    def __str__(self):
        return f"Caja[{self.codigo}] - {self.descripcion_carga}, peso={self.peso_kg}kg, dimensiones={self.largo}x{self.ancho}x{self.altura}m"


class Camion:
    def __init__(self, matricula, conductor, capacidad_kg, descripcion_carga, rumbo, velocidad):
        self.matricula = matricula
        self.conductor = conductor
        self.capacidad_kg = capacidad_kg
        self.descripcion_carga = descripcion_carga
        self.rumbo = rumbo
        self.velocidad = velocidad
        self.cajas = []

        if not (1 <= self.rumbo <= 359):
            raise ValueError("El rumbo debe estar entre 1 y 359 grados.")

    def peso_total(self):
        total = 0
        for caja in self.cajas:
            total += caja.peso_kg
        return total

    def add_caja(self, caja):
        if self.peso_total() + caja.peso_kg <= self.capacidad_kg:
            self.cajas.append(caja)
            print(f"Añadida {caja.codigo} al camión {self.matricula}. Peso total: {self.peso_total()} kg")
        else:
            print(f"No se puede añadir {caja.codigo}. Capacidad superada.")

    def setVelocidad(self, nueva_velocidad):
        self.velocidad = nueva_velocidad

    def setRumbo(self, nuevo_rumbo):
        if 1 <= nuevo_rumbo <= 359:
            self.rumbo = nuevo_rumbo
        else:
            print("Rumbo fuera de rango. No se actualiza.")

    def claxon(self):
        print("piiiiiii")

    def __str__(self):
        texto = f"Camión {self.matricula} | Conductor: {self.conductor}\n"
        texto += f"Capacidad: {self.capacidad_kg} kg | Peso actual: {self.peso_total()} kg | Nº cajas: {len(self.cajas)}\n"
        texto += f"Rumbo: {self.rumbo}° | Velocidad: {self.velocidad} km/h\n"
        texto += "Cajas:\n"
        if self.cajas:
            for caja in self.cajas:
                texto += "  - " + str(caja) + "\n"
        else:
            texto += "  (sin cajas)\n"
        return texto


def main():
    # Crear cajas iniciales
    cajas_camion1 = [
        Caja("C1-A", 500, "Electrodomésticos", 1.2, 0.8, 0.7),
        Caja("C1-B", 300, "Textil", 1.0, 0.6, 0.5),
        Caja("C1-C", 200, "Libros", 0.9, 0.5, 0.4),
    ]

    cajas_camion2 = [
        Caja("C2-A", 600, "Herramientas", 1.1, 0.7, 0.6),
        Caja("C2-B", 250, "Juguetes", 0.8, 0.6, 0.5),
        Caja("C2-C", 150, "Papelería", 0.7, 0.5, 0.4),
    ]

    # Crear camiones
    camion1 = Camion("CA-1234-AB", "María", 1500, "Rutas urbanas", 90, 60)
    camion2 = Camion("CA-5678-CD", "Juan", 1800, "Ruta interurbana", 270, 80)

    # Añadir cajas iniciales
    for caja in cajas_camion1:
        camion1.add_caja(caja)
    for caja in cajas_camion2:
        camion2.add_caja(caja)

    print("\n--- Información inicial ---")
    print(camion1)
    print(camion2)

    # Añadir más cajas
    nuevas_cajas_1 = [
        Caja("C1-D", 400, "Pequeña maquinaria", 1.3, 0.9, 0.8),
        Caja("C1-E", 200, "Material oficina", 0.9, 0.6, 0.5),
    ]
    nuevas_cajas_2 = [
        Caja("C2-D", 500, "Bebidas", 1.2, 0.8, 0.7),
        Caja("C2-E", 300, "Repuestos", 1.0, 0.7, 0.6),
        Caja("C2-F", 400, "Alimentos secos", 1.1, 0.8, 0.7),
    ]

    for caja in nuevas_cajas_1:
        camion1.add_caja(caja)
    for caja in nuevas_cajas_2:
        camion2.add_caja(caja)

    # Cambiar velocidad y rumbo
    camion1.setVelocidad(75)
    camion1.setRumbo(120)
    camion2.setVelocidad(90)
    camion2.setRumbo(300)

    # Claxon del segundo camión
    camion2.claxon()

    print("\n--- Información final ---")
    print(camion1)
    print(camion2)


if __name__ == "__main__":
    main()
