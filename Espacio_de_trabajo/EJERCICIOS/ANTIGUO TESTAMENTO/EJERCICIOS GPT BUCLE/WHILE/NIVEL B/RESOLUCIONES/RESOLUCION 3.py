'''Tabla de multiplicar:
Solicita al usuario ingresar un número y utiliza un bucle while para imprimir la tabla de multiplicar de ese número.'''


n = int(input('Ingresa un numero: '))

contador = 0
print(f'La tabla de multiplicar del {n} es: ')
while contador < n:
    contador+= 1
    print(f'{contador} x {n} = {contador*n}')
    