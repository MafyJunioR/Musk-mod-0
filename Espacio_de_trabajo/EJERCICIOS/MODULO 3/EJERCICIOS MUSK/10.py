class Estudiante:
    
    def __init__(self, nombre, edad, grado):
        
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
    def asistencias(self,meses_asistencias):
        return self._asistencias_(meses_asistencias)

    def _asistencias_(self, meses_asistencias):
        for asistencias in meses_asistencias.values():
            if asistencias < 4:
                return 1
            elif 4 < asistencias <= 8:
                return 2
            else:
                return 3
            
alumno1 = Estudiante('George', 26, 0)

asistencias_mes = {
    'enero' : 3,
    'febrero': 6,
    'marzo': 8
}

print(alumno1.asistencias(asistencias_mes))