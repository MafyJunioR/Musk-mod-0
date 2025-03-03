'''
Ejercicio 7: Contar dígitos de un número
Escribe un programa que pida al usuario un número entero positivo y cuente cuántos dígitos tiene el número usando un bucle `while`.
'''


n = int(input('Ingresa un numero: '))

cuantos_numeros = 0

while n > 0:
    n //= 10
    cuantos_numeros +=1
print(cuantos_numeros)