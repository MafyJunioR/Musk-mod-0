'''Imprimir números en reversa:
Pide al usuario que ingrese un número e imprime los números desde ese número hasta 1 en orden descendente utilizando un bucle for.'''

n = int(input('Ingresa un numero: '))

for i in range(n, 0-1, -1):
    print(i)