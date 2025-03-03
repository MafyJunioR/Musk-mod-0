'''### Ejercicio 2: Contador de Vocales
Escribe un programa que tome una cadena de texto como entrada del usuario
y use un bucle para contar cuántas vocales (a, e, i, o, u) hay en la cadena.
Muestra el conteo para cada vocal.'''


texto = (input('Escribe un texto: '))

suma_vocal_a = 0
suma_vocal_e = 0
suma_vocal_i = 0
suma_vocal_o = 0
suma_vocal_u = 0

for vocal in texto:
    if vocal == 'a' or vocal == 'A':
        suma_vocal_a += 1
    elif vocal == 'e' or vocal == 'E':
        suma_vocal_e += 1
    elif vocal == 'i' or vocal == 'I':
        suma_vocal_i += 1
    elif vocal == 'o' or vocal == 'O':
        suma_vocal_o += 1
    elif vocal == 'u' or vocal == 'U':
        suma_vocal_u += 1
        
print(f'Cantidad de vocales a: {suma_vocal_a}')
print(f'Cantidad de vocales e: {suma_vocal_e}')
print(f'Cantidad de vocales i: {suma_vocal_i}')
print(f'Cantidad de vocales o: {suma_vocal_o}')
print(f'Cantidad de vocales u: {suma_vocal_u}')