'''1. Haz un programa que lea dos números a y b, y que escriba todos los números enteros a y b. 
Debe cumplirse que a < b. En caso que a > b, escribe los número de manera descendente.'''


a = int(input('Introduce un numero: '))
b = int(input('Introduce un numero: '))


if a == b:
    print('Introduce numeros distintos anda.')
elif a < b:
    for i in range(a,b +1):
        print(i)
else:
    for i in range(a,b - 1, -1):
        print(i)