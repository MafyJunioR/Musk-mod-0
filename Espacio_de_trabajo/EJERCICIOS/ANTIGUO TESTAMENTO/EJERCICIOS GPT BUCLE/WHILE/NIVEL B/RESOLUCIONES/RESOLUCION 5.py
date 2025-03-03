'''Solicita al usuario ingresar un límite superior.
Utiliza un bucle `while` para calcular la suma de los 
números del 1 al límite ingresado.'''

n = int(input('Ingresa un numero: '))

contador = 0

while contador < n:
    contador+= 1
    print(contador)