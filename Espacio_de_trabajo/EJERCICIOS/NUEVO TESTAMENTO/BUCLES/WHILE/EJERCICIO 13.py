'''
Ejercicio 13: Contar vocales en una cadena
Escribe un programa que pida al usuario una cadena de texto y 
cuente cuántas vocales (a, e, i, o, u) hay en la cadena usando un bucle `while`.
'''


texto = input('Ingresa un texto: ')

suma_a = 0
suma_e = 0
suma_i = 0
suma_o = 0
suma_u = 0

indice = 0


while indice < len(texto):
    if texto[indice] == 'a' or texto[indice] == 'A':
        suma_a += 1
    
    if texto[indice] == 'e' or texto[indice] == 'E':
        suma_e += 1
    
    if texto[indice] == 'i' or texto[indice] == 'I':
        suma_i += 1
    
    if texto[indice] == 'o' or texto[indice] == 'O':
        suma_o += 1
    
    if texto[indice] == 'u' or texto[indice] == 'U':
        suma_u += 1
    indice += 1





print(f'La letra a aparece {suma_a} veces')
print(f'La letra e aparece {suma_e} veces')
print(f'La letra i aparece {suma_i} veces')
print(f'La letra o aparece {suma_o} veces')
print(f'La letra u aparece {suma_u} veces')