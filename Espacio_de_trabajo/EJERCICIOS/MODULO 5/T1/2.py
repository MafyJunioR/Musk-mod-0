def contar_lineas():
    try:
        with open('story.txt', 'r', encoding='utf-8') as archivo:
            contador = 0
            for linea in archivo:
                contador += 1
            print(f'El numero de lineas es {contador}')
    except FileNotFoundError:
        print('El archivo ''story.txt'' no se encuentra.')
        
contar_lineas()