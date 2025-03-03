'''Calcular factorial:
Pide al usuario que ingrese un número y calcula su factorial utilizando un bucle for.'''

n = int(input('Ingresa un numero: '))

multiplicacion = 1

for i in range(1, n+1):
    multiplicacion *= i
    
print(f'El factorial del numero {n} es {multiplicacion}')