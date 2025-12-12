import time

# --- CLASES BASE Y COMPONENTES ---

class Capitan:
    def __init__(self, nombre, rango):
        self.nombre = nombre
        self.rango = rango

    def __str__(self):
        return f"{self.rango} {self.nombre}"

class Sistema:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo  # Ej: 'Arma', 'Sensor', 'Defensa'

    def __str__(self):
        return f"{self.tipo}: {self.nombre}"

# --- CLASE PADRE (PLATAFORMA) ---

class Plataforma:
    def __init__(self, nombre, matricula):
        self.nombre = nombre
        self.matricula = matricula
        self.capitan = None
        self.sistemas = []  
        self.estado_operativo = True
        self.vida = 100
        self.rumbo = 0
        self.velocidad = 0

    def asumir_mando(self, capitan):
        self.capitan = capitan
        print(f"El {capitan} ha asumido el mando del {self.nombre}.")

    def agregar_sistema(self, sistema):
        self.sistemas.append(sistema)

    def navegar(self, rumbo, velocidad):
        self.rumbo = rumbo
        self.velocidad = velocidad
        print(f"[{self.nombre}] Navegando a rumbo {rumbo} con velocidad {velocidad} nudos. [cite: 22]")

    def recibir_danio(self, cantidad):
        self.vida -= cantidad
        print(f"¡ALERTA! [{self.nombre}] ha recibido {cantidad} de daño. Vida restante: {self.vida}% [cite: 24]")
        if self.vida <= 0:
            self.estado_operativo = False
            print(f"[{self.nombre}] ha sido DESTRUIDA.")

    def esta_operativa(self):
        estado = "OPERATIVA" if self.estado_operativo else "FUERA DE COMBATE"
        print(f"Estado de [{self.nombre}]: {estado} [cite: 27]")
        return self.estado_operativo

    def atacar(self):
        if self.estado_operativo:
            print(f"[{self.nombre}] disparando sus sistemas de armas...")

    def __str__(self):
        cap_info = str(self.capitan) if self.capitan else "Sin Capitán"
        sys_info = ", ".join([s.nombre for s in self.sistemas])
        return f"Nave: {self.nombre} ({type(self).__name__}) | Cap: {cap_info} | Sys: {sys_info} | Vida: {self.vida}%"

# --- CLASES HIJAS (HERENCIA) ---

class Fragata(Plataforma):
    def despegar_helicoptero(self):
        if self.estado_operativo:
            print(f"[{self.nombre}] Despegando helicóptero de reconocimiento... [cite: 26]")

class Submarino(Plataforma):
    def sumergirse(self, profundidad):
        if self.estado_operativo:
            print(f"[{self.nombre}] Sumergiéndose a {profundidad} metros. [cite: 25]")

class Corbeta(Plataforma):
    def maniobra_evasiva(self):
        if self.estado_operativo:
            print(f"[{self.nombre}] Realizando maniobra evasiva rápida.")

# --- AGREGACIÓN (FLOTA) ---

class Flota:
    def __init__(self, nombre_flota):
        self.nombre = nombre_flota
        self.plataformas = []  # Lista de plataformas

    def agregar_plataforma(self, plataforma):
        self.plataformas.append(plataforma)

    def ordenar_ataque(self):
        print(f"\n--- LA FLOTA {self.nombre.upper()} ORDENA UN ATAQUE GENERAL [cite: 21] ---")
        for p in self.plataformas:
            p.atacar()

    def mostrar_informacion(self):
        print(f"\n--- ESTADO DE LA {self.nombre.upper()} [cite: 16] ---")
        for p in self.plataformas:
            print(p) # Muestra datos, capitanes y sistemas 
        print("-" * 50)

if __name__ == "__main__":
    print("INICIANDO SIMULADOR NAVAL...\n")

    
    cap1 = Capitan("Ramírez", "Capitán de Navío")
    cap2 = Capitan("Johnson", "Teniente")
    cap3 = Capitan("Volkov", "Comandante")

    
    fragata = Fragata("F-100 Álvaro de Bazán", "F100")
    corbeta = Corbeta("C-20 Atrevida", "C20")
    submarino = Submarino("S-80 Isaac Peral", "S80")

    
    canon = Sistema("Cañón 76mm", "Arma")
    misil = Sistema("Harpoon", "Arma")
    sonar = Sistema("Sonar Activo", "Sensor")
    radar = Sistema("Radar Aéreo", "Sensor")

    fragata.agregar_sistema(misil)
    fragata.agregar_sistema(radar)
    corbeta.agregar_sistema(canon)
    submarino.agregar_sistema(sonar)

    
    fragata.asumir_mando(cap1)
    corbeta.asumir_mando(cap2)
    submarino.asumir_mando(cap3)

    
    flota_atlantico = Flota("Flota del Atlántico")
    flota_atlantico.agregar_plataforma(fragata)
    flota_atlantico.agregar_plataforma(corbeta)
    flota_atlantico.agregar_plataforma(submarino)

    
    flota_atlantico.mostrar_informacion()

    
    input("Presione Enter para iniciar la simulación de batalla...")
    
    flota_atlantico.ordenar_ataque() 
    
    fragata.navegar(90, 20)        
    submarino.navegar(180, 10)
    
    corbeta.recibir_danio(40)       
    
    submarino.sumergirse(200)       
    fragata.despegar_helicoptero()  
    
   
    corbeta.recibir_danio(70)        

    print("\n--- REPORTE DE DAÑOS ---")
    fragata.esta_operativa()         
    corbeta.esta_operativa()
    submarino.esta_operativa()


    flota_atlantico.mostrar_informacion()