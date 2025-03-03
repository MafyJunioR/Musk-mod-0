def annadir_texto(texto):
        with open('story.txt', 'a', encoding='utf-8') as archivo:
            archivo.write(f'{texto}')
        with open('story.txt', 'r') as archivo:
            contenido = archivo.read()
            print(contenido)

        
        
annadir_texto('Este texto lo acabo de añadir.\n')
annadir_texto('Y este también.\n')