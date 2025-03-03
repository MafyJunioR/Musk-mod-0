'''
Ejercicio 14: Generar una tabla de multiplicar
Escribe un programa que pida al usuario un número entero positivo y genere la tabla de multiplicar de ese número hasta 10 usando un bucle `while`.
'''

conteo = 1

n = int(input('Escribe un numero: '))

print(f'La tabla de multiplicar de {n} es: ')
while conteo <= 10:
    print(f'{conteo} x {n} = {conteo * n}')
    conteo += 1
    