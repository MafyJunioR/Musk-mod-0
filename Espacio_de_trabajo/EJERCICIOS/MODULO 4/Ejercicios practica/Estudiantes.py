class Estudiante:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.calificaciones = []
        
    def agregar_calificaciones(self, calificacion):
        self.calificaciones.append(calificacion)
        
    def calcular_promedio(self):
        if len(self.calificaciones) > 0:
            return sum(self.calificaciones) / len(self.calificaciones)
        else:
            return None
        
    def describir(self):
        promedio = self.calcular_promedio()
        if promedio is not None:
            return f'Estudiante: {self.nombre}. Edad: {self.edad}. Media: {promedio}'
        else:
            return f'Estudiante: {self.nombre}. Edad: {self.edad}. Media: No hay calificaciones.'
        
estudiante1 = Estudiante('Luis', 20)
estudiante2 = Estudiante('Sara', 26)

estudiante1.agregar_calificaciones(9.2)
estudiante1.agregar_calificaciones(6.8)
estudiante2.agregar_calificaciones(9.1)

print(estudiante1.describir())
print(estudiante2.describir())

estudiante2.agregar_calificaciones(4.6)
print(estudiante2.describir())