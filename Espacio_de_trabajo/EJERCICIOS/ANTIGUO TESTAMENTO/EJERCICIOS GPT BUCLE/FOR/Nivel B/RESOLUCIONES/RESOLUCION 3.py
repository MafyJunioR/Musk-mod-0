'''Ejercicio 3: Tabla de Multiplicar
Escribe un programa que solicite al usuario ingresar un número entero. 
Luego, usa un bucle `for` para imprimir la tabla de multiplicar de ese número desde 1 hasta 10.'''

n = int(input('Ingresa un numero y te enseñaré su tabla de multiplicar: '))

print(f'La tabla de multiplicar de {n} es: ')
for i in range(1, 11):
    print(f'{i} X {n} = {i*n}')