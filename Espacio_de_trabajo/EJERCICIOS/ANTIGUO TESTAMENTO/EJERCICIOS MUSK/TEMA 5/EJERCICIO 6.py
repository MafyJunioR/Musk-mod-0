'''6. Haz un programa que encuentre la última posición de una subcadena dada.'''


texto = input('Ingresa un texto: ')
palabra = input('Ingresa una palabra a buscar: ')


donde = texto.rfind(palabra)


print(f'La ultima vez que la palabra {palabra} aparece, es en la posicion {donde}.')