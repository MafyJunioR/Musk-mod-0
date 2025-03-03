'''Contador de cifras:

Pide al usuario que ingrese un número entero y 
utiliza un bucle while para contar la cantidad de cifras en ese número.'''

n = int(input('Ingresa un numero: '))

conteo = 0

if n == 0:
    conteo = 1

while n != 0:
    conteo += 1
    n //= 10
    
print(f'El numero tiene {conteo} cifras')