'''Crea una clase base DispositivoElectronico que tenga:

Atributos: marca, modelo, encendido (booleano, inicializado como False).
Métodos:
encender: Cambia el estado de encendido a True.
apagar: Cambia el estado de encendido a False.
Crea una clase base Conectividad que tenga:

Atributos: conexion (almacena el tipo de conexión: "WiFi", "Bluetooth", etc., por defecto None).
Métodos:
conectar: Recibe el tipo de conexión y lo asigna a conexion.
desconectar: Limpia el atributo conexion.
Crea la siguiente clases derivadas utilizando herencia múltiple:

Smartphone:
Hereda de DispositivoElectronico y Conectividad.
Métodos:
hacer_llamada: Recibe un número de teléfono como parámetro y muestra un mensaje indicando que se está llamando a ese número (solo si el dispositivo está encendido).'''

class DispositivoElectronico:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False
        
    def encender(self):
        self.encendido = True
        
    def apagar(self):
        self.encendido == False
        
class Conectividad:
    def __init__(self):
        self.conexion = None
        
    def conectar(self, tipo_conexion):
        self.conexion = tipo_conexion
        
    def desconectar(self):
        self.conexion = None
        
class SmartPhone(DispositivoElectronico, Conectividad):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        
    def hacer_llamada(self, numero):
        if self.encendido == True:
            print(f'Está llamando a\n {numero}')
        else:
            print('____________________Obviamente no va.')
            
            
movil = SmartPhone('Samsung', 'S25')

print('\n\nIntentando llamar sin enceder el móvil. Jeje')
movil.hacer_llamada(697218932)
print('Encendiendo móvil')
movil.encender()
print('Segundo intento de llamada con el movil encendido ya.')
movil.hacer_llamada(697218932)