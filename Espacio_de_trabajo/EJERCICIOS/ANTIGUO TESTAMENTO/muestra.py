alumnos = {}

while True:
    opcion = input('Introducir nuevas notas? (si/no): ')

    if opcion == 'no':
        break
    
    elif opcion == 'si':
        estudiante = input('Nombre del alumno: ')
    
        cantidad_notas = int(input('Número de notas a introducir: '))
        lista_notas = []

        for nota in range (cantidad_notas):
          calificacion = int(input('Introduzca una nota: '))
          lista_notas.append(calificacion)

        alumnos[estudiante] = lista_notas
    else:
        print('Elija una opcion (si o no)')
    
print(alumnos)

'''14.	Sobre el ejercicio anterior, calcula la media de cada estudiante y guarda la media de cada uno en un nuevo diccionario. 
Una vez calculada la media de cada alumno realiza las siguientes acciones:'''

media_alumnos = {}

for estudiante, notas in alumnos.items():
    media = sum (notas)/len(notas)
    media_alumnos [estudiante] = media

print(media_alumnos)
#1. Crea una lista con los alumnos con medias inferiores a 5 y otra con notas iguales o superiores a 5.
media_inferior = []
media_superior = []

for estudiante, media in media_alumnos.items():
    if media < 5:
        media_inferior.append(estudiante)   
    else:
        media_superior.append(estudiante)   

print(f'Estos alumnos tienen una media superior a 5: {media_superior}') 
print(f'Estos alumnos tienen una media inferior a 5: {media_inferior}')

#2. Calcula la media global de la clase
media_global = sum(media_alumnos.values())/len(media_alumnos.values())
print(f'La media global de la clase es de {media_global}')

#3.	Modifica la media de cada alumno por: Insuficiente si la media es menor que 5, Notable si está en 5 y 8 y Sobresaliente si la nota es mayor de 8.
media_palabras = {}

for estudiante, media in media_alumnos.items():
    if media < 5:
        media_palabras[estudiante] = 'Insuficiente'
    elif 5 <= media < 8:
        media_palabras[estudiante] = 'Notable'
    else:
        media_palabras[estudiante] = 'Sobresaliente'

print(media_palabras)

#4.	Crea un nuevo diccionario en el que la clave sea Insuficiente, Notable o Sobresaliente y el valor el numero de alumnos que tienen esas calificaciones
media_calificaciones = {}
alumnos = 0

for estudiante, palabra in media_palabras.items():
    if palabra == 'Insuficiente':
        alumnos += 1
        media_calificaciones ['Insuficiente'] = alumnos
    elif palabra == 'Notable':
        alumnos += 1
        media_calificaciones ['Notable'] = alumnos
    elif palabra == 'Sobresaliente':
        alumnos += 1
        media_calificaciones ['Sobresaliente'] = alumnos

print(media_calificaciones)