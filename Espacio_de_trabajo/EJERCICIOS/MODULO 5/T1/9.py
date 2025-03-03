def contar_palabras():
    try:
        with open('story.txt', 'r', encoding='utf-8') as archivo:
            frecuencia = {}
            for linea in archivo:
                palabras = linea.split()
                for palabra in palabras:
                    if palabra in frecuencia:
                        frecuencia[palabra] +=1
                    else:
                        frecuencia[palabra] = 1
            print(f'Cada palabra se repiten estas veces: {frecuencia}')
    except FileNotFoundError:
        print('El archivo ''story.txt'' no se encuentra.')
        
contar_palabras()