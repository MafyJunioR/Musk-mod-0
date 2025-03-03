'''
Ejercicio 3: Adivina el número
Escribe un programa que genere un número aleatorio entre 1 y 100, y pida al usuario adivinarlo. 
El programa debe continuar pidiendo al usuario que adivine hasta que adivine correctamente.
'''


import random
numero_secreto = random.randint(1, 100)
numero = 0



while numero != numero_secreto:
    numero = int(input('Ingresa un número del 1 al 100: '))
    if numero < numero_secreto:
        if numero_secreto <= 25:
            print('El número secreto está entre 1 y 25. Sube mas.')
        elif numero_secreto <= 50:
            print('El número secreto está entre 26 y 50. Sube mas.')
        elif numero_secreto <= 75:
            print('El número secreto está entre 51 y 75. Sube mas.')
        elif numero_secreto <= 100:
            print('El número secreto está entre 76 y 100. Sube mas.')
    elif numero > numero_secreto:
        print('Demasiado alto. Intenta otra vez.')
    else:
        print('BINGO')