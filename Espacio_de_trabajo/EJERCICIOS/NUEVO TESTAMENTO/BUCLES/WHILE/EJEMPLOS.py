''''''
'1. Contar hasta un número específico.'
'''
contador = 1
while contador <= 10:
    print(contador)
    contador += 1

'''
'2. Sumar números hasta cierto límite.'
'''
suma = 0
numero = 1
while numero <= 100:
    suma += numero
    numero += 1
print("La suma de los números del 1 al 100 es:", suma)

'''
'3. Adivinar un número.'
'''
import random
numero_secreto = random.randint(1, 100)
adivinanza = None
while adivinanza != numero_secreto:
    adivinanza = int(input("Adivina el número (entre 1 y 100): "))
    if adivinanza < numero_secreto:
        print("Demasiado bajo. Intenta de nuevo.")
    elif adivinanza > numero_secreto:
        print("Demasiado alto. Intenta de nuevo.")
    else:
        print("¡Felicidades! Adivinaste el número.")

'''
'4. Calcular el promedio de una serie de números.'
'''
suma = 0
contador = 0
numero = 0
while numero >= 0:
    numero = float(input("Ingresa un número (negativo para terminar): "))
    if numero >= 0:
        suma += numero
        contador += 1
if contador > 0:
    promedio = suma / contador
    print("El promedio de los números ingresados es:", promedio)
else:
    print("No se ingresaron números positivos.")

'''
'5. Generar los primeros n números de la serie de Fibonacci.'
'''
n = int(input("Ingresa la cantidad de números de la serie de Fibonacci que deseas ver: "))
a, b = 0, 1
contador = 0
while contador < n:
    print(a)
    a, b = b, a + b
    contador += 1

'''
'6. Invertir un número.'
'''
numero = int(input("Ingresa un número entero positivo: "))
numero_invertido = 0
while numero > 0:
    digito = numero % 10
    numero_invertido = numero_invertido * 10 + digito
    numero //= 10
print("El número invertido es:", numero_invertido)
'''
