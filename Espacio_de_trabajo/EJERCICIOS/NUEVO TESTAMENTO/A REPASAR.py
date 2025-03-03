'''Ejercicios de Bucles
Imprimir números del 1 al 10:
Escribe un programa que use un bucle for para imprimir los números del 1 al 10.
'''
for i in range(1,11):
    print(i)
print('_________________________________________________________---------------------------------------------')    

'''Suma de números del 1 al 100:
Escribe un programa que use un bucle for para calcular la suma de los números del 1 al 100.
'''

suma = 0

for i in range(1,100 +1):
    suma += i
    print(suma)   

print('_________________________________________________________---------------------------------------------')    



'''Imprimir elementos de una lista:
Dada la lista frutas = ['manzana', 'plátano', 'cereza'], escribe un programa que use un bucle for para imprimir cada fruta en la lista.
'''
frutas = ['manzana', 'plátano', 'cereza']

for palabra in frutas:
    print(palabra)




print('_________________________________________________________---------------------------------------------')  

'''Ejercicios de Diccionarios
Acceder a valores en un diccionario:
Dado el diccionario alumno = {'nombre': 'Juan', 'edad': 20, 'carrera': 'Informática'}, escribe un programa que imprima cada clave y su valor.'''

alumno = {
    'nombre': 'Juan',
    'edad': 20,
    'carrera': 'Informática'}

for clave, valor in alumno.items():
    print(f'{clave}: {valor}')

print('_________________________________________________________---------------------------------------------')  


'''Contar ocurrencias de palabras:
Escribe un programa que cuente la cantidad de veces que cada palabra aparece en la lista 
palabras = ['manzana', 'plátano', 'manzana', 'cereza', 'plátano', 'plátano']
y almacene los resultados en un diccionario.'''

frutas = ['manzana', 'plátano', 'manzana', 'cereza', 'plátano', 'plátano']

inventario = {}

for palabra in frutas:
    if palabra in inventario:
        inventario[palabra] += 1
    else:
        inventario[palabra] = 1

print(inventario)        
print('_________________________________________________________---------------------------------------------')  


'''Añadir y eliminar elementos:
Dado el diccionario inventario = {'manzanas': 5, 'plátanos': 8},
escribe un programa que añada una nueva entrada para cerezas con un valor de 12 y luego elimine la entrada de manzanas.
'''

inventario = {'manzanas': 5, 'plátanos': 8}


inventario.update({'cerezas': 12})

inventario.__delitem__('manzanas')
print(inventario)

print('_________________________________________________________---------------------------------------------')  


'''Ejercicios de Condicionales
Determinar si un número es par o impar:
Escribe un programa que tome un número como entrada y determine si es par o impar.'''

x = int(input('Ingresa un numero: '))

if x % 2 == 0:
    print(f'{x} es par.')
else:
    print(f'{x} es impar.')





'''
Clasificación por edad:
Escribe un programa que tome una edad como entrada y clasifique a la persona en una categoría: niño (0-12), adolescente (13-17), adulto (18-64) o mayor (65+).
'''
#Muy facil este.


'''
Verificar una contraseña:
Escribe un programa que pida al usuario que ingrese una contraseña y
verifique si es correcta (define la contraseña correcta en el código). '''

contrasenna_base_datos = 'Bl4ck@p5'
print('''Bienvenido, ingrese usuario y contraseña.
        
            USUARIO: MAFYJUNIOR
         CONTRASEÑA: ''')

contrasenna_ingresada = input('Ingrese la contraseña: ')

if contrasenna_ingresada == contrasenna_base_datos:
    print('Iniciando sesión.')
else:
    print('Vuelva a intentarlo.')
    
