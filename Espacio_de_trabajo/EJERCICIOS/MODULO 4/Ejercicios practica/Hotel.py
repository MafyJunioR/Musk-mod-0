class Habitacion:
    def __init__(self, numero, tipo, precioxnoche):
        
        self.numero = numero
        self.tipo = tipo
        self.precioxnoche = precioxnoche
        self.reservada = False
        
    def hacer_reserva(self):
        if not self.reservada:
            self.reservada = True
            return f'Habitacion {self.numero} reservada con éxito'
        else:
            return f'Habitacion {self.numero} ya reservada.'
        
    def cancelar_reserva(self):
        if self.reservada:
            self.reservada = False
            return f'Habitacion {self.numero} cancelada con éxito'
        else:
            return f'Habitacion {self.numero} ya estaba disponible.'
        
    def describir(self):
        if self.reservada == True:
            estado = 'Reservada'
        else:
            estado = 'Lista para reservar\n'
        return f'____\nNº Habitacion: {self.numero}. Tipo: {self.tipo}. \nPrecio/noche: {self.precioxnoche}. Reservada?: {estado}.'
    
habitacion1 = Habitacion(101, 'Individual', 50)
habitacion2 = Habitacion(201, 'Doble', 100)
habitacion3 = Habitacion(301, 'Suite', 175)

print(habitacion1.describir())
print(habitacion2.describir())
print(habitacion3.describir())

print(habitacion1.hacer_reserva())
print(habitacion2.hacer_reserva())
print(habitacion3.cancelar_reserva())

print(habitacion1.describir())
print(habitacion2.describir())
print(habitacion3.describir())

print(habitacion2.hacer_reserva())
print(habitacion2.describir())