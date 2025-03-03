'''Ejercicio 4: Calculadora de promedio
Escribe un programa que pida al usuario ingresar números hasta que ingrese un número negativo.
Luego, el programa debe calcular y mostrar el promedio de los números ingresados (sin contar el número negativo).'''


numeros = []

while True:
    ingresa_numeros = int(input('Ingresa 1 numero: '))
    numeros.append(ingresa_numeros)
    if len(numeros) == 3:
        ingresa_numeros = int(input('Ahora añade un numero negativo: '))
        if ingresa_numeros < 0:
            print(sum(numeros) / len(numeros))
            break
            


