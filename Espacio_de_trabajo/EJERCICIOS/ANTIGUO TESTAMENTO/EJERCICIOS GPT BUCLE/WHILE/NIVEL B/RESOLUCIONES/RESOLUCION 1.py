'''Suma de dígitos:
Solicita al usuario ingresar un número entero 
y utiliza un bucle while para calcular la suma de sus dígitos.'''

n = int(input('Ingresa un numero mayor que 10: '))

suma = 0

while n != 0:
    digito = n % 10
    suma += digito
    n //= 10
    print(f'La suma de los digitos es: {suma}')
    
