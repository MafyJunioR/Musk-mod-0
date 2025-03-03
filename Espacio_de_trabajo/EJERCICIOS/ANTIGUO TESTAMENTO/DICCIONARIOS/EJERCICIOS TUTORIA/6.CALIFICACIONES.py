'''Calculadora de calificaciones: Crea un programa que solicite al usuario ingresar nombres de estudiantes y sus calificaciones, y luego genere un diccionario 
donde los nombres son las claves y las calificaciones son los valores (estas calificaciones tienen que ser una lista de notas de cada estudiante).
El programa debe permitir al usuario buscar las calificaciones de un estudiante específico.

SEGUNDA PARTE 
Sobre el ejercicio anterior, calcula la media de cada estudiante y guarda la media de cada uno en un nuevo diccionario.
Una vez calculada la media de cada alumno realiza las siguientes acciones:
Crea una lista con los alumnos con medias inferiores a 5 y otra con notas iguales o superiores a 5.
Calcula la media global de la clase
Modifica la media de cada alumno por: Insuficiente si la media es menor que 5, Notable si está en 5 y 8 y Sobresaliente si la nota es mayor de 8.
Crea un nuevo diccionario en el que la clave sea Insuficiente, Notable o Sobresaliente y el valor el numero de alumnos que tienen esas calificaciones.'''





#diccionarios vacios
calificaciones = {}
media_notas = {}

#MENÚ
while True:
    menu = int(input(''' Que quieres hacer?
                     1. Agregar nuevos alumnos. 
                     2.Ver notas de alguien en concreto.
                     3.Ver media de un alumno en concreto. 
                     4.Ver cuaderno de medias 
                     5.Salir 
                     -'''))
    if menu ==  1:
# funcion para introducir nombres a los diccionarios
        while True:
            pregunta = input('Quieres agregar un nuevo alumno? (si o no): ')
            
            if pregunta.lower() == 'si':
                nombre = (input('Introduce el nombre del siguiente alumno: '))
                calificaciones[nombre.lower()] = []
                media_notas[nombre.lower()] = []
                print(f'Alumno {nombre} añadido.')
                
                cantidad_notas = int(input(f'Cuantas notas tiene {nombre}? '))
                for i in range(cantidad_notas):
                    nota = float(input(f'Introduce la nota {i + 1} para {nombre}: '))
                    
                    calificaciones[nombre.lower()].append(nota)
                    media = sum(calificaciones[nombre.lower()]) / cantidad_notas
                    media_notas[nombre.lower()] = [media]
                    
                
            elif pregunta.lower() == 'no':
                while True:
                    quieres_ver = input('Quieres ver el cuaderno de calificaciones? (si o no): ')
                    if quieres_ver.lower() == 'no':
                        print('OK,chao.')
                        break
                    elif quieres_ver.lower() == 'si':
                        print(f'El cuaderno de calificaciones es este: {calificaciones}')
                        break
                break
            else:
                print('Recuerda, solo ''si'' o ''no''.')
                
    elif menu == 2:
        
        while True:
            alumno_especifico = input('Quieres ver las notas de alguien en concreto? (''si'' o ''no''): ')
            
            if alumno_especifico.lower() == 'si':
                busca = input('De quien?: ').lower()
                if busca in calificaciones:
                    print(f'Las notas de {busca} son: {calificaciones[busca]}')
                else:
                    print(f'El nombre {busca} no existe.')
                    break
            elif alumno_especifico.lower() == 'no':
                break
            else:
                print('Introduce ''si'' o ''no''. ')
                
    elif menu == 3:
        
        while True:
            quiere_nota = input('Quieres ver la media de alguien? (''si'' o ''no''): ')
            
            if quiere_nota.lower() == 'si':
                busca_media = input('De quien?:').lower()
                if busca_media in calificaciones:
                    
                    print(f'La media de {busca_media} es: {media_notas[busca_media]} ') 
                else:
                    print(f'{busca_media} no tiene notas.')
                    
            elif quiere_nota.lower() == 'no':
                break
            else:
                print('Introduce ''si'' o ''no''.')    
                
                
    elif menu == 4:
        
        while True:
            quiere_media = input('Quieres ver el cuaderno de medias? (''si'' o ''no''): ')
            
            if quiere_media.lower() == 'si':
                print(media_notas)
                break
            elif quiere_media.lower() =='no':
                break
            else:
                print('Introduce ''si'' o ''no''.')
    elif menu == 5:
        print('Hasta luego.')
        break
    else:
        print('Elige entre 1, 2, 3 ó 4.')
