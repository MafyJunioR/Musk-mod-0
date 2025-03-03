'''6. Haz un programa que lea un número y que escriba el número de dígitos.'''


n = int(input('Introduce un numero: '))
x = n
conteo = 0

while n > 0:
    n = n // 10
    conteo += 1
print(f'El numero {x} tiene {conteo} cifras')