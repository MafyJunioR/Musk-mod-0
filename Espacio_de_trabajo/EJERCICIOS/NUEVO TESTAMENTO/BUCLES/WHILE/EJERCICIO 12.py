'''
Ejercicio 12: Sumar una serie de números
Escribe un programa que pida al usuario un número entero positivo `n` y
luego sume todos los números del 1 al `n` usando un bucle `while`.
'''


n = int(input('Ingresa un numero: '))
contador = 1
suma = 0

while contador <= n:
    suma += contador
    contador+= 1
print(suma)