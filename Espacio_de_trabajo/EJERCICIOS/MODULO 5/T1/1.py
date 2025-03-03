def leer_archivo():
    try:
        with open('poema.txt', 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                print(linea.strip())
    except FileNotFoundError:
        print('El archivo ''poema.txt'' no se encuentra.')