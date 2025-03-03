#Escribir un programa que pregunte al usuario su edad
# y muestre por pantalla si es mayor de edad o no.

#edad = int(input('Ingrese su edad: '))
#if edad >= 18:
#    print('Eres mayor de edad')
#else:
#    print('Eres menor de edad')
    
    
    
    
#Escribir un programa que almacene la cadena de caracteres contraseña
# en una variable, pregunte al usuario por la contraseña e imprima 
# por pantalla si la contraseña introducida por el usuario coincide 
# con la guardada en la variable.

#contrasenna_introducida = str(input('Ingresa contraseña: '))
#contrasenna_almacenada = '1234abc'

#if contrasenna_almacenada == contrasenna_introducida:
#    print('Iniciando sesión')
#else:
#    print('Haz memoria e ingresa nuevamente')

#Escribe un programa que solicite al usuario ingresar su edad y si 
# tiene un carnet de estudiante (responde "s" para sí y "n" para no.
# verificar si la persona es menor de 25 años y tiene un carnet de 
# estudiante. Si ambas condiciones se cumplen, imprime "
# Eres elegible para el descuento de estudiante", de lo contrario,
# imprime "No eres elegible para el descuento de estudiante".

#edad = int(input('Ingresa tu edad: '))
#carnet_estudiante = input('Tienes carnet de estudiante?')

#if edad <= 25 and carnet_estudiante == 'SI'
#    print('Eres elegible para el descuento de estudiante')
#else:
#    print('No eres elegible para el descuento de estudiante')


#Clasificación de Edad: Solicita al usuario que ingrese su edad
# y clasifícala en "niño" (0-12 años), "adolescente" (13-17 años),
# "adulto joven" (18-25 años), "adulto" (26-64 años), o "adulto mayor"
# (65 años en adelante).

#edad = int(input('Ingresa edad: '))

#if edad >= 0 and edad <= 12:
#    print('Eres un niño')
#elif edad >= 13 and edad <= 17:
#    print('Eres un adolescente ')
#elif edad >= 18 and edad <= 25:
#    print('Eres adulto joven')
#elif edad >= 26 and edad <= 64:
#    print('Eres adulto')
#elif edad >= 64:
#    print('Eres adulto')


'''Número Positivo o Negativo: Escribe un programa que solicite 
al usuario ingresar un número e imprima si el número es positivo, negativo o cero.'''


#n = int(input('Ingresa un numero: '))

#if n!= 0:
#    if n < 0:
#        print(f'{n} es negativo')
#    else:
#        print('El numero es positivo')
#else:
#    print('0 es 0')
    
    
# Or

#n = int(input('Ingresa un numero: '))

#if n > 0:
#    print(f'{n} es positivo')
#elif n < 0:
#    print(f'{n} es negativo')
#else:
#    print('El numero es cero')

'''Comparación de Tres Números con or: 
Solicita al usuario que ingrese tres números e imprime si al menos uno de ellos es positivo.'''

x = int(input('Ingresa un numero: '))
y = int(input('Ingresa otro numero: '))
z = int(input('Otro mas y ya: '))

if x > 0 or y > 0 or z > 0:
    print('Por lo menos un numero es positivo, vamos a ver cual.')
    if x > 0:
        print(f'{x} es positivo.')
    if y > 0:
        print(f'{y} es positivo.')
    if z > 0:
        print(f'{z} es positivo.')
else:
    print('Ninguno de los números es positivo.')