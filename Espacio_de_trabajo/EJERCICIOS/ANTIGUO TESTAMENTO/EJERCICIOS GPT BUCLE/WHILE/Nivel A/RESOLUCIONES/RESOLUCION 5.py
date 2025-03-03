'''Solicita al usuario un número entero positivo e imprime los números pares desde 2 hasta ese número.'''

n = int(input('Ingresa un numero: '))

contador = 2

while contador <= n:
    print(contador)
    contador += 2