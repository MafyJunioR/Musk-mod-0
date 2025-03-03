def localizar_archivo(documento):
    try:
        with open(documento, 'r', encoding='utf-8') as archivo:
            print('El archivo existe.')
    except FileNotFoundError:
        print(f'El archivo {documento} no existe.')
        
        
localizar_archivo('materia.txt')
localizar_archivo('archivo que no existe.txt')