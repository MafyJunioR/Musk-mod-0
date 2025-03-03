class Vehiculo:
    
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        
    def describir(self):
        return f'Vehículo {self.marca}, {self.modelo}. Año: {self.año}'
    
    def encender(self):
        print('El vehículo está encendido.')
        
    def apagar(self):
        print('El vehículo está apagado.')
        
class Automovil(Vehiculo):
    
    def __init__(self, marca, modelo, año, combustible):
        super().__init__(marca, modelo, año)
        self.combustible = combustible
        
    def describir(self):
        return f'Vehículo {self.marca}, {self.modelo}. Año: {self.año}. Combustible: {self.combustible}'
    
    def tocar_bocina(self):
        print('3,14 ** 2')
        
class Bicicleta(Vehiculo):
    
    def __init__(self, marca, modelo, año, tipo):
        super().__init__(marca, modelo, año)
        self.tipo = tipo #montaña o ciudad
        
    def describir(self):
        return f'Vehículo {self.marca}, {self.modelo}. Año: {self.año}. Tipo: {self.tipo}'
    
    def pedalear(self):
        print('La bicicleta se mueve.')
        
class Garaje:
    
    def __init__(self):
        self.vehiculos = []
        
    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
        
    def mostrar_vehiculos(self):
        for vehiculo in self.vehiculos:
            print(vehiculo.describir())
            
    def encender_todos(self):
        for vehiculo in self.vehiculos:
            vehiculo.encender()
            
    def apagar_todos(self):
        for vehiculo in self.vehiculos:
            vehiculo.apagar()
            
            
auto1 = Automovil("Toyota", "Corolla", 2007, "Gasolina")
auto2 = Automovil("Tesla", "Model S", 2022, "Eléctrico")
bici1 = Bicicleta("Giant", "Talon", 2019, "Montaña")


garaje = Garaje()
garaje.agregar_vehiculo(auto1)
garaje.agregar_vehiculo(auto2)
garaje.agregar_vehiculo(bici1)


garaje.mostrar_vehiculos()


garaje.encender_todos()


garaje.apagar_todos()


auto1.tocar_bocina()
bici1.pedalear()