class Vuelos:
    def __init__(self, numero_vuelo, aerolinea, destino, hora_salida):
        self.numero_vuelo = numero_vuelo
        self.aerolinea = aerolinea
        self.destino = destino
        self.hora_salida = hora_salida
        self.estado = 'Programado.'
        
    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
        
    def actualizar_hora_salida(self, nueva_hora):
        self.hora_salida = nueva_hora
        
    def describir(self):
        return f'\nNumero Vuelo: {self.numero_vuelo}.\nAerolinea: {self.aerolinea}.\nDestino de vuelo: {self.destino}.\nHora salida: {self.hora_salida}.\nEstado:{self.estado}\n'
    
vuelo1 = Vuelos('AA123','Iberia','Otopeni', '18:30')
vuelo2 = Vuelos('AA124', 'WizzAir', 'Bilbao', '14:00')

print(vuelo1.describir())
print(vuelo2.describir())

vuelo1.actualizar_hora_salida('19:00')
vuelo1.cambiar_estado('Retrasado.')
print(vuelo1.describir())
