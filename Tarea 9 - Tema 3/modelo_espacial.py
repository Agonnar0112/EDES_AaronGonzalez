import time

class SistemaPropulsion:
    def __init__(self, tipo_combustible, cantidad, empuje_max):
        self.tipo_combustible = tipo_combustible
        self.cantidad = cantidad
        self.empuje_max = empuje_max

    def consumir(self, cantidad):
        if self.cantidad >= cantidad:
            self.cantidad -= cantidad
            return True
        print("¡Combustible insuficiente!")
        return False

class SistemaComunicacion:
    def __init__(self, potencia, frecuencias):
        self.potencia = potencia
        self.frecuencias = frecuencias
        self.operativo = True

    def enviar_mensaje(self, msg):
        if self.operativo:
            print(f"[COMMS]: Enviando '{msg}' a {self.potencia}W")
        else:
            print("[COMMS]: Error, sistema averiado.")

class ObjetoEspacial:
    def __init__(self, nombre, x, y, vx, vy):
        self.nombre = nombre
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def avanzar_tiempo(self):
        self.x += self.vx
        self.y += self.vy

    def __str__(self):
        return f"{self.nombre} en ({self.x}, {self.y})"

class CuerpoNatural(ObjetoEspacial):
    def __init__(self, nombre, x, y, vx, vy, masa, tipo, sistema_origen):
        super().__init__(nombre, x, y, vx, vy)
        self.masa = masa
        self.tipo = tipo
        self.sistema_origen = sistema_origen

class Planeta(CuerpoNatural):
    def __init__(self, nombre, x, y, vx, vy, masa, sistema, radio, max_satelites, atmosfera):
        super().__init__(nombre, x, y, vx, vy, masa, "Planeta", sistema)
        self.radio = radio
        self.max_satelites = max_satelites
        self.atmosfera = atmosfera

class SateliteNatural(CuerpoNatural):
    def __init__(self, nombre, x, y, vx, vy, masa, sistema, orbitando_a, distancia):
        super().__init__(nombre, x, y, vx, vy, masa, "Satélite Natural", sistema)
        self.orbitando_a = orbitando_a
        self.distancia = distancia

class EstructuraArtificial(ObjetoEspacial):
    def __init__(self, nombre, x, y, vx, vy, agencia, pais, estado):
        super().__init__(nombre, x, y, vx, vy)
        self.agencia = agencia
        self.pais = pais
        self.estado = estado
        self.motor = SistemaPropulsion("Hidracina", 1000, 500)
        self.radio = SistemaComunicacion(200, ["UHF", "S-Band"])
        self.centro_control = None 

    def asignar_control(self, centro):
        self.centro_control = centro

class Cohete(EstructuraArtificial):
    def __init__(self, nombre, x, y, vx, vy, agencia, pais, empuje_total, carga_max):
        super().__init__(nombre, x, y, vx, vy, agencia, pais, "En plataforma")
        self.empuje_total = empuje_total
        self.carga_max = carga_max
        self.lanzamientos = 0

    def lanzar(self):
        if self.motor.consumir(100):
            self.estado = "En lanzamiento"
            self.lanzamientos += 1
            print(f"🚀 {self.nombre} ha despegado.")

class SateliteArtificial(EstructuraArtificial):
    def __init__(self, nombre, x, y, vx, vy, agencia, pais, orbitando_a, funcion):
        super().__init__(nombre, x, y, vx, vy, agencia, pais, "Inactivo")
        self.orbitando_a = orbitando_a
        self.funcion = funcion



class SistemaPlanetario:
    def __init__(self, nombre, estrella):
        self.nombre = nombre
        self.estrella = estrella
        self.cuerpos = [] 

    def agregar_cuerpo(self, cuerpo):
        self.cuerpos.append(cuerpo)

    def mostrar_info(self):
        print(f"--- Sistema {self.nombre} (Estrella: {self.estrella}) ---")
        for c in self.cuerpos:
            print(f"  - {c}")

# --- CONTROL (ASOCIACIÓN) ---

class CentroControl:
    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais
        self.misiones = []

    def registrar_mision(self, nave):
        self.misiones.append(nave)
        nave.asignar_control(self)
        print(f"Control {self.nombre} asume mando de {nave.nombre}")
        
if __name__ == "__main__":
    print("=== INICIANDO SIMULACIÓN DE CONSOLA ===\n")

    sis_solar = SistemaPlanetario("Sistema Solar", "Sol")
    tierra = Planeta("Tierra", 0, 0, 0, 0, 5.97e24, "Sistema Solar", 6371, 1, True)
    luna = SateliteNatural("Luna", 10, 5, 1, 0, 7.34e22, "Sistema Solar", "Tierra", 384400)
    
    sis_solar.agregar_cuerpo(tierra)
    sis_solar.agregar_cuerpo(luna)

    houston = CentroControl("Johnson Space Center", "USA")
    
    cohete1 = Cohete("Falcon 9", 0, 0, 0, 10, "SpaceX", "USA", 7600, 22800)
    sat1 = SateliteArtificial("Hubble", 0, 600, 5, 0, "NASA", "USA", "Tierra", "Observación")

    houston.registrar_mision(cohete1)
    houston.registrar_mision(sat1)

    print("\n--- ESTADO INICIAL ---")
    sis_solar.mostrar_info()
    print(f"Nave: {cohete1.nombre} | Combustible: {cohete1.motor.cantidad} | Estado: {cohete1.estado}")


    print("\n... Ejecutando simulación ...")
    luna.avanzar_tiempo()   
    cohete1.lanzar()          
    sat1.avanzar_tiempo()
    sat1.estado = "En órbita" 

    
    print("\n--- ESTADO FINAL ---")
    print(luna) 
    print(sat1)
    print(f"Nave: {cohete1.nombre} | Combustible: {cohete1.motor.cantidad} | Estado: {cohete1.estado}")