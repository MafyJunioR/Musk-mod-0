'''Cree un diccionario de estudiantes y agregue nombre, apellido, 
sexo, edad, estado civil, habilidades, país, ciudad y dirección como claves para el diccionario.
Obtener la longitud del diccionario del estudiante
Obtenga el valor de las habilidades y verifique el tipo de datos, debería ser una lista
Modifique los valores de las habilidades agregando una o dos habilidades.
Obtenga las claves del diccionario como una lista
Obtener los valores del diccionario como una lista'''

estudiantes = {
    'nombre': 'Fernando',
    'apellido': 'Alonso',
    'sexo': 'Masculino',
    'edad': '33',
    'estado civil': 'casado',
    'habilidades': ['conducir','adelantar', 'ganar'],
    'pais': 'España',
    'ciudad': 'Asturias',
    'dirección': 'Calee El Cristo, n1'
}

print(len(estudiantes))

habilidades = estudiantes['habilidades']
print(habilidades)
print(type(habilidades))
estudiantes['habilidades'].append('celebrar')
print(habilidades)

claves = estudiantes.keys()
valores = estudiantes.values()

print(f'La lista de claves del diccionario estudiantes es: {list(claves)}')
print(f'La lista de valores del diccionario estudiantes es: {list(valores)}')