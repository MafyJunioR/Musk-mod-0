'''
Ejercicio 15: Número perfecto
Escribe un programa que pida al usuario un número entero positivo y determine si el número es perfecto.
Un número es perfecto si es igual a la suma de sus divisores propios (excluyendo el número mismo) usando un bucle `while`.
'''

n = int(input('Ingresa un numero y verás si es perfecto o no: '))

conteo = 1
resultado = 0
numeros_perfectos = []
while conteo <= n:
    if resultado == n // conteo or resultado == conteo // n:
        numeros_perfectos.append(resultado)
print(numeros_perfectos)