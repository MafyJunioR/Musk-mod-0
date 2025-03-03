'''
Ejercicio 11: Calcular el factorial de un número
Escribe un programa que pida al usuario un número entero positivo y 
calcule el factorial de ese número usando un bucle `while`.
'''

n = int(input('Ingresa un numero: '))
factorial = 1
contador = 1
while contador <= n:
    factorial *= contador
    contador += 1
print(factorial)