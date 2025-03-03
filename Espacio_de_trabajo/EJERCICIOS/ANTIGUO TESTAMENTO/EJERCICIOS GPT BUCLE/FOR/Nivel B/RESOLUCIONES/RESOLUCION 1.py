'''Ejercicio 1: Suma de Números Pares
Escribe un programa que solicite al usuario ingresar un número entero positivo `n`. 
Luego, utiliza un bucle para calcular la suma de todos los números pares desde 2 hasta `n` (incluyendo `n`).
Muestra el resultado.'''


n = int(input('Ingresa un numero positivo: '))

suma_pares = 0

for i in range(2, n + 1, 2):
     suma_pares += i
    
print(suma_pares)