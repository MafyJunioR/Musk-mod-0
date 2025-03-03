'''
Crea un diccionario llamado `info_estudiante` 
que tenga la siguiente información para un estudiante:
- Nombre
- Edad
- Carrera
- Lista de materias que está cursando
(por ejemplo, ["Matemáticas", "Física", "Programación"])

Luego, realiza lo siguiente:
1. Accede al nombre del estudiante e imprímelo.
2. Imprime la edad del estudiante.
3. Agrega una nueva materia a la lista de materias.
4. Imprime el diccionario completo.
'''

diccionario = {
    'Nombre': 'George',
    'Edad': '26',
    'Carrera': 'Bachiller',
    'Lista de materias' : ['Mates', 'Fisica', 'Historia']
    
}
nombre_estudiante = diccionario['Nombre']
print(f'El nombre del estudiante es: {nombre_estudiante}')

edad_estudiante = diccionario['Edad']
print(f'La edad del estudiante es: {edad_estudiante}')

diccionario['Lista de materias'].append('Quimica')

print(f'Todo sobre el estudiante: {diccionario}')