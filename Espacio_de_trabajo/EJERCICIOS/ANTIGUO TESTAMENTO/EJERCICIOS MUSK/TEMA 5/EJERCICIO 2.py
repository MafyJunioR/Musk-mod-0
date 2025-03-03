'''2. Haz un programa que encuentre todas las apariciones de una subcadena en una cadena dada.'''



texto = input('Introduce un frase: ')
subtexto = input('Palabra a buscar en la frase: ')

cuantas_veces = texto.count(subtexto.lower( ))


print(f'La palabra {subtexto} aparece {cuantas_veces} veces en la frase introducida.')