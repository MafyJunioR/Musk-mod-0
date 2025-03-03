'''4. Haz un programa que lea n palabras, y que escriba cada una invirtiendo la orden de sus caracteres.'''

lista_palabrs = []

n= int(input('Cuantas palabras vas a escribir?: '))

for i in range(1, n+1):
    palabra = input(f'Escribe la {i}º palabra: ')
    palabras_reves = palabra[::-1]
    lista_palabrs.append(palabras_reves)

print(lista_palabrs)

