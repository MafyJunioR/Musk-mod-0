'''Contar Caracteres: Crea un diccionario que cuente la frecuencia
de cada carácter en una cadena de texto.'''


texto = 'Hola mundo.'

suma_consonantes = 0
suma_vocal = 0

for vocal in texto:
    if vocal == 'a' or vocal == 'A' or vocal == 'e' or vocal == 'E' or vocal == 'i' or vocal == 'I' or vocal == 'o' or vocal == 'O' or vocal == 'u' or vocal == 'U':
        suma_vocal += 1

