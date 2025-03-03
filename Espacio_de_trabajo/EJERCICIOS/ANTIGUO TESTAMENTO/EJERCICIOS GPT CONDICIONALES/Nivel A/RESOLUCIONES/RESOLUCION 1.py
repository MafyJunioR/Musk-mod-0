'''1. **Número positivo o negativo:**
   Solicita al usuario que ingrese un número y 
   muestra un mensaje indicando si es positivo o negativo.'''


numero = int(input('Ingresa un numero (negativo o positivo): '))

if numero < 0:
    print('Es un numero negativo')
else:
    print('Es un numero positivo')