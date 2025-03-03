def hash_display():
    try:
        with open('materia.txt', 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                textohash = '#'.join(linea.strip())
                        # ó   linea.replace('', '#') 
                print(textohash)
                
    except FileNotFoundError:
        print('El archivo ''materia.txt'' no se encuentra.')
        
        
hash_display()