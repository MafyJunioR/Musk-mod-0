'''6.Pide al usuario que ingrese un número y utiliza un bucle while para calcular el factorial de ese número.'''


n = int(input('Ingresa un numero y te diré el factorial: '))

factorial = 1
contador = 1

while contador <= n:
    print (contador)
    contador *= factorial
    break