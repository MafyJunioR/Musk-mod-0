class Estudiante:
    
    escuela = 'IES Txurdinaga Behekoa'
    
    def __init__(self, nombre, edad, grado):
        
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    @classmethod
    def cambiar_escuela(cls, nueva_escuela):
        
        cls.escuela = nueva_escuela
        
alumno1 = Estudiante('George', 26, 0)
alumno2 = Estudiante('Ianire', 22, 0)

print(alumno1.escuela)
print(alumno2.escuela)

Estudiante.cambiar_escuela('IES Gabries Aresti')

print(alumno1.escuela)
print(alumno2.escuela)