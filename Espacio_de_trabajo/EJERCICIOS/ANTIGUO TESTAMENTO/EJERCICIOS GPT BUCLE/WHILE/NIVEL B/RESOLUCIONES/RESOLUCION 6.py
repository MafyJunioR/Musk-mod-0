'''Solicita al usuario ingresar un número entero
y utiliza un bucle `while` para contar la cantidad
de dígitos en ese número.'''

n = int(input('Ingresa un numero: '))

suma = 0

if n == 0:
    suma +=1
    
while n != 0:
    suma += 1
    n //=10
    
print(f'El numero tiene {suma} cifras')