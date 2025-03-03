def display_words():
    try:
        with open('story.txt', 'r', encoding='utf-8') as archivo:
            palabras4 = []
            for linea in archivo:
                palabras = linea.split()
                for palabra in palabras:
                    if len(palabra) < 4:
                        palabras4.append(palabra)
            print(f'Las palabras con menos de 4 caracteres son: {palabras4}')
    except FileNotFoundError:
        print('El archivo ''story.txt'' no se encuentra.')
        
        
display_words()