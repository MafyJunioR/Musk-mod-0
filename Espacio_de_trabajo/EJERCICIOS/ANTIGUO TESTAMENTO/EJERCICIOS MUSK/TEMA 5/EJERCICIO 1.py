'''1. Haz un programa que lea una secuencia de caracteres acabada en punto y que escriba cuántas letras ‘a’ contiene.'''


texto = input('Introduce una frase: ')
letra_a = 0
for letra in texto: 
    if letra == 'a':
        letra_a += 1
print(f'En la frase introducida hay {letra_a} as.')