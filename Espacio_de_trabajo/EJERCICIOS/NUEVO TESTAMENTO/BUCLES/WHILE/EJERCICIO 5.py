'''Ejercicio 5: Serie de Fibonacci
Escribe un programa que genere los primeros `n` números de la serie de Fibonacci, donde `n` es un número entero ingresado por el usuario.'''


a ,b = 0, 1
contador = 1
n = int(input('Ingresa cuantos numeros de fibonacci quieres ver: '))
while contador <= n:
    print(a)
    a, b= b, a+b
    contador += 1