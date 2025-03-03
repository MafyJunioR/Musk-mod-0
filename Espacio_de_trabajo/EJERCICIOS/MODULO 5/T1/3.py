def contar_palabras():
    try:
        with open('story.txt', 'r', encoding='utf-8') as archivo:
            contador_palabras = 0
            for linea in archivo:
                palabras = linea.split()
                contador_palabras += len(palabras)
            print(f'El numero de palabras en este archivo es: {contador_palabras}')
    except FileNotFoundError:
        print('El archivo ''story.txt'' no se encuentra.')