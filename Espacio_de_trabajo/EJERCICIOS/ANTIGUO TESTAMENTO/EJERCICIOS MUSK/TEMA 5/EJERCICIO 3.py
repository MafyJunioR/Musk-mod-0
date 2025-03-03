'''3. Haz un programa que invierta una cadena dada.'''


texto = input('Ingresa un texto: ')

al_reves = ''.join(reversed(texto))


print(al_reves)

# Ó evitando la linea de codigo '6', escribes directamente:

print(texto[::-1])  ### Esta línea imprime directamente la cadena invertida.


'''texto[start:end:step]: Esta es la sintaxis general de slicing.

texto[::-1]: Aquí, start y end están vacíos, lo que significa que toma toda la cadena.

El step es -1, lo que indica que se recorre la cadena desde el principio hasta el final en pasos de -1, o sea, de atrás hacia adelante, invirtiendo la cadena.

print(texto[::-1]): Esta línea imprime directamente la cadena invertida.'''