'''Sumar elementos de una lista:
Crea una lista de números y utiliza un bucle for para calcular la suma de todos los elementos de la lista.'''

n = int(input('Ingresa un numero para ver cuanto suman todos sus numeros anteriores: '))

suma = 0

for i in range(1, n + 1):
    suma += i
print(suma)