'''
Ejercicio 8: Sumar dígitos de un número
Escribe un programa que pida al usuario un número entero positivo y calcule la suma de sus dígitos usando un bucle `while`.
'''

n = int(input('Ingresa un numero: '))
suma = 0
numero_guardado = n
while n > 0:
    digito = n % 10
    suma = suma + digito
    n //= 10
print(f'La suma de los digitos de {numero_guardado} es {suma}')