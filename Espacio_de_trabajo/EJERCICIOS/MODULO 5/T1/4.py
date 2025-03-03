def buscar_palabra(palabra):
    try:
        with open('poema.txt', 'r', encoding='utf-8') as archivo:
            encontrado = False
            for numero_linea, linea in enumerate(archivo, start=1):
                if palabra.lower() in linea.lower().split():
                    encontrado = True
                    print(f'La palabra {palabra} se encontró en la linea {numero_linea}: {linea.strip()}.')
            if not encontrado:
                print('La palabra no se ha encontrado.')
                
    except FileNotFoundError:
        print('El archivo ''poema.txt'' no se encuentra.')
        
        
buscar_palabra('el')