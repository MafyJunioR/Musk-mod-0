calificaciones = {}
media_notas = {}

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
                
while True:
            quiere_nota = input('Quieres ver la media de alguien? (''si'' o ''no''): ')
            
            if quiere_nota.lower() == 'si':
                busca_media = input('De quien?:').lower()
                if busca_media in media_notas:
                    
                    print(f'La media de {busca_media} es: {media_notas[busca_media][0]} ') # EJECUTA EL PROGRAMA Y AGREGA 2 PERSONAS Y PIDELE LA MEDIA DE CADA UNO INDEPENDIENTEMENTE, TE LA DARÁ MAL DANDOTE LA MEDIA DEL ULTIMO SIEMPRE
                else:
                    print(f'{busca_media} no tiene notas.')
                    
            elif quiere_nota.lower() == 'no':
                break
            else:
                print('Introduce ''si'' o ''no''.')