'''Escribe un programa que solicite al usuario ingresar un número entero `n` 
y utilice un bucle para calcular el factorial de `n` 
(el producto de todos los enteros positivos hasta `n`). Muestra el resultado.'''


n = int(input('Ingresa un numero y te diré el factorial: '))

print(f'{n}! es: ')

factorial = 1
for i in range(1, n+1):
    factorial *= i
    
print(factorial)