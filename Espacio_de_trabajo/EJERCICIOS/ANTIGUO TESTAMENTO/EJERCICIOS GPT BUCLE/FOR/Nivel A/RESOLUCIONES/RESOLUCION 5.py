'''Contar letras en una palabra:
Solicita al usuario que ingrese una palabra y utiliza un bucle for para contar y mostrar la cantidad de letras en esa palabra.'''


palabra = (input('Escribe una palabra y te diré cuantas letras tiene: '))

cuantas_letras = 0

for letras in palabra:
    cuantas_letras += 1
    
print(f'La palabra {palabra} tiene {cuantas_letras} letras')