'''4. Haz un programa que divida una cadena en guiones.'''


texto = input('Escribe-una-frase-asi: ')

texto2 = texto.split('-')
for palabra in texto2:
    print(palabra)