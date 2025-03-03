'''
Dado un texto como entrada, crea una función llamada `conteo_palabras` 
que cuente la frecuencia de cada palabra en el texto y devuelva un diccionario con esta información. 
Los caracteres no alfabéticos no deben considerarse como parte de las palabras.

texto = "La programación en Python es divertida. Python es un lenguaje versátil y popular."

1. Crea la función que tome el texto como parámetro y devuelva el diccionario con el conteo de palabras.
2. Llama a la función con el texto de ejemplo e imprime el resultado.
'''

import re
texto = "La programación en Python es divertida. Python es un lenguaje versátil y popular."
palabras = texto.split()
conteo_palabras = 0

for palabra in palabras:
    conteo_palabras += 1
print(conteo_palabras)


#########   CHUNGUISIMO     #########
#########   Voy mal, Cosas pendientes por aprender todavia      #########