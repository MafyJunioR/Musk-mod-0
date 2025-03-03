def prod(l1, l2):
    solution = []
    
    def generador():
        for i in range(min(len(l1), len(l2))):
            yield l1[i] * l2[i]
    
    gen = generador()

    try:
        while True:
            solution.append(next(gen))
    except StopIteration:
        pass
    
    return solution


l1 = list(range(1, 11123))
l2 = list(range(1, 11))
resultado = prod(l1, l2)
print(resultado)


print('\n______________________________________\n')
print('\n______________________________________\n')
print('\n______________________________________\n')


import random

def generar_aleatorio():
    contador = 1
    n = int(input('Cuantos numeros aleatorios quieres?: '))
    while contador <= n:
        aleatorio = random.randint(1, 100)
        yield aleatorio
        contador += 1
        
for numero in generar_aleatorio():
    print(numero)
    
print('\n______________________________________\n')
print('\n______________________________________\n')
print('\n______________________________________\n')


def Fib():

    n = int(input('Ingresa un numero: '))

    lista = [0,1]
    contador = 0
    for i in range(n-2):
        x = lista[-1] + lista[-2]
        lista.append(x)
        contador +=1
        yield lista
        
for numero in Fib():
    pass
print(numero)

print('\n______________________________________\n')
print('\n______________________________________\n')
print('\n______________________________________\n')

def Multiplicacionx2():

    n = int(input('Ingresa un numero: '))


    contador = 0
    for i in range(1,n):
        contador += 1
        multiplicacion = i *2
        yield multiplicacion
        
for numero in Multiplicacionx2():
    print(numero)
    
    
print('\n______________________________________\n')
print('\n______________________________________\n')
print('\n______________________________________\n')


import random

def generar_aleatorio():
    contador = 1
    n = int(input('Cuantos numeros aleatorios quieres?'))
    while contador <= n:
        aleatorio = random.randint(-10**10, 10**10) #estoy simulando un rango sin limite, ya que con random randint hay que poner un rango entre a y b
        if aleatorio % 2 != 0:
            yield aleatorio
            contador += 1
        
        
for numero in generar_aleatorio():
    print(numero)