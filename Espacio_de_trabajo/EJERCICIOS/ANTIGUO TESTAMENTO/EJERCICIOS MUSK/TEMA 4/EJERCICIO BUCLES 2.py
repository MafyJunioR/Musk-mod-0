'''2. Haz un programa que lea una secuencia números entre 'a' y 'b' y que escriba la media.'''
a = int(input('Introduce un numero:'))
b = int(input('Introduce un numero mas grande que el anterior: '))
suma = 0
cantidad = 0


'''if b <= a :
    print('Hablo chino papi?')
else:
    for i in range(a,b +1):
        suma += i
        cantidad += 1
    media = suma / cantidad
        
print(media)
print(cantidad)'''



if b > a:
    for i in range(a,b +1):
        suma += i
        cantidad += 1
    media = suma / cantidad
    print(media)
    print(cantidad)

    
else:
    print('Hablo chino papi?')
    
