'''
Ejercicio 9: Encontrar el máximo y mínimo de una lista
Escribe un programa que pida al usuario ingresar números hasta que ingrese un número negativo.
Luego, el programa debe encontrar y mostrar el número máximo y mínimo de los números ingresados
(sin contar el número negativo).
'''

numeros = []


while True:
    ingresa_numeros = int(input('Ingresa 1 numero: '))
    numeros.append(ingresa_numeros)
    if len(numeros) == 3:
        ingresa_numeros = int(input('Ahora añade un numero negativo: '))
        if ingresa_numeros < 0:
            print(f'El numero mas grande de los numeros ingresados es {max(numeros)}')
            print(f'El numero mas pequeño de los numeros ingresados es {min(numeros)}')
            
            break
        
        