'''9.Llame a su función factorial,
toma un número entero como parámetro y 
devuelve un factorial del número'''



def factorial(n):
    multiplicacion = 1
    
    for i in range(1, n+1):
        multiplicacion *= i
        
    return multiplicacion



print(factorial(9))