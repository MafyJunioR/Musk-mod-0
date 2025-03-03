'''1.	Declarar una lista vacía
2.	Declarar una lista con más de 7 elementos
3.	Encuentra la longitud de tu lista'''

#1
mi_lista = []

#2
mi_lista_7 = ['cobre', 'oro', 'plata', 'rodio', 'aluminio', 'plutonio', 'uranio']

#3
print(len(mi_lista_7))

'''4.Corta tu lista, muestra los 2 primeros elementos, luego muestra los dos últimos
5.	Obtenga el primer elemento, el elemento del medio y el último elemento de la lista.'''

#4
print(mi_lista_7[:2:])

print(mi_lista_7[0],mi_lista_7[1])

print(mi_lista_7[-1],mi_lista_7[-2])

#5
print(mi_lista_7[0])
print(mi_lista_7[4])
print(mi_lista_7[-1])


#7

'''Suma de elementos: Escribe un programa que sume todos los elementos de una lista de números enteros.'''


lista_num = [1,2,3,4,5]

suma = 0

for numeros in lista_num:
    suma += numeros
print(suma)