'''Solicita al usuario ingresar un número entero positivo
y utiliza un bucle `while` para calcular su factorial.'''

n = int(input('Ingresa un numero: '))

multiplicacion = 1
contador = 0
while contador < n:
    contador +=1
    multiplicacion*= contador
print(multiplicacion)