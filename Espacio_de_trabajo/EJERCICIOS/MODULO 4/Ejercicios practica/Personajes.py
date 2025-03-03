class Personaje:

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa        
        self.vida = vida
         
    def atributos(self):
        print(f'Nombre:  {self.nombre}')
        print(f'Fuerza: {self.fuerza}')
        print(f'Inteligencia: {self.inteligencia}')
        print(f'Defensa: {self.defensa}')
        print(f'Vida: {self.vida}')
        
    def subir_nivel(self, fuerza, inteligencia, defensa, vida):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
        
    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0
        print(f'{self.nombre} ha muerto')
        
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa
    
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(f'{self.nombre}, ha realizado {daño}, puntos de daño a {enemigo.nombre}')
        print(f'La vida de {enemigo.nombre} es {enemigo.vida}')
        if enemigo.esta_vivo():
            print(f'La vida de: {enemigo.nombre}, es {enemigo.vida}')
        else:
            enemigo.morir()
        
mi_personaje = Personaje('MafyJunioR', 10, 1, 5, 100)
mi_enemigo = Personaje('Enemigo 1', 8, 5, 3, 1)
print(mi_personaje.esta_vivo())
mi_personaje.atacar(mi_enemigo)
print(mi_enemigo.atributos())

