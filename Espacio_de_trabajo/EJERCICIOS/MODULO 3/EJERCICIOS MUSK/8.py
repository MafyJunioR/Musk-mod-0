class Estudiante:
    
    def __init__(self, nombre, edad, grado):
        
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
        
    @staticmethod
    
    def inferior5(cuaderno_notas):
        for materia, nota in cuaderno_notas.items():
            if nota < 5:
                print(f'{materia} : {nota}')
            
            
alumno1 = Estudiante('George', 26, 0)
asignaturas = {
    'Lengua' : 8,
    'Mates' : 5,
    'Inglés': 4,
    'Historia' : 3,
    'Recreo': 1
}

Estudiante.inferior5(asignaturas)
