'''mprimir patrón de asteriscos:
Utiliza un bucle for para imprimir el siguiente patrón de asteriscos:


*
**
***
****
***** '''

n = int(input('Ingresa un numero: '))

cadena_asterisco = 1

for i in range(1, n + 1):
    cadena = cadena_asterisco * i * '*'
    print(cadena)
    
# Esa es la version complicada
# Y esta es la sencilla:

# n = int(input('Ingresa un número: '))

# for i in range(1, n + 1):
#     print('*' * i)