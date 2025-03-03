'''Suma de números pares:
Calcula la suma de los números pares del 1 al 'n' utilizando un bucle for.'''

n = int(input('Introduce un numero: '))

suma_numeros = 0

for i in range(1, n+1):
    if i % 2 == 0:
        suma_numeros += i

print(suma_numeros)