class Estudiante:
    
    def __init__(self, nombre, edad, grado):
        
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
        
    def calcular_media(self, notas):
        if notas:
            self.grado = sum(notas) / len(notas)
        else:
            self.grado = 0
    
alumno1 = Estudiante('George', 26, 0)

notas = [9,8,7.5,6,8.8]


alumno1.calcular_media(notas)

print(f'{alumno1.nombre} : {alumno1.grado}')