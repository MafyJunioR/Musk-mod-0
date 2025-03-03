'''1. Haz un programa que cree una función en Python que dada una secuencia devuelva únicamente los números pares.'''



def dar_par(*lista):
    pares = []
    for numeros in lista:
        if numeros % 2 == 0:
            pares.append(numeros)
    return pares


print(dar_par(1,2,3,4,5,6,7,8,9,22,24,28,29,1000))