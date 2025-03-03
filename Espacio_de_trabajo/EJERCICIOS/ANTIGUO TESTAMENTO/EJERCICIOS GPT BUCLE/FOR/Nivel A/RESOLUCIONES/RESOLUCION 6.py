'''Imprimir números pares en un rango:
Pide al usuario que ingrese un número y utiliza un bucle for para imprimir todos los números pares desde 0 hasta ese número.'''


n = int(input('Ingresa un numero: '))

print(f'Los numeros pares desde el 0 hasta el {n} son: ')

for i in range(0, n+1):
    if i % 2 == 0:
     print(i)