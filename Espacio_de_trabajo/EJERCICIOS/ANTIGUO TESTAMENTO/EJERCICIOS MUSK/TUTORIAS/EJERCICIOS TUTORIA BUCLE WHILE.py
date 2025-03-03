'''Imprimir Números: Imprime los números del 1 al 10.'''

'''contador = 1

while contador <= 10:
    print(contador)
    contador +=1  '''
    
'''Tabla de Multiplicar Específica: 
Pide al usuario un número y luego imprime la tabla de multiplicar de ese número del 1 al 10.'''

'''n = int(input('Ingresa un numero: '))

contador = 0
print(f'La tabla de multiplicar del {n} es: ')

while contador <= 10:
    print(f'{n} x {contador} = {contador * n}')
    contador +=1'''
    
    
'''Contar letras:
Pide al usuario una palabra y cuenta cuántas letras hay en esa palabra.'''

'''texto = (input('Ingresa una palabra y te diré cuantas letras tiene: '))

contador = 0

while contador < len(texto):
   contador += 1
print(contador)'''


'''Escriba un programa que pregunte una y otra vez si desea continuar 
con el programa, siempre que se conteste exactamente sí (en minúsculas y con tilde).'''


'''respuesta = (input('Tienes hambre?'))
while respuesta == 'si':
    respuesta = input('Tienes hambre?')
else:
    print('Vale, perdón :(')'''
    
'''Patrón de Estrellas:
Imprime el siguiente patrón de estrellas:
*
**
***  
**** 
*****'''


'''contador = 1

while contador <= 5:
    print(contador * '*')
    contador += 1'''
    
    
    
'''6-	Adivina el número: Escribe un programa que genere un número aleatorio entre 1 y 100.
Luego, pídele al usuario que adivine el número. Si el usuario adivina correctamente, 
muestra un mensaje de felicitaciones y termina el juego. Si no, sigue pidiéndole al usuario que ingrese otro número hasta que adivine correctamente.
'''
import random
numero_secreto = random.randint(1, 10)
n = int(input('Vamos a jugar: '))

while True:
    if numero_secreto == n:
        print(f'Muy bien! El numero era: {numero_secreto}')
    else:
        int(n)