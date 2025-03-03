'''Escriba una función llamada add_all_nums que tome un número 
arbitrario de argumentos y los sume todos.
Compruebe si todos los elementos de la lista son tipos numéricos.
Si no, dé una valoración razonable.'''
 
 
 
def add_all_nums(*numeros):
    total = 0
    
    for num in numeros:
        if type(num) == int or type(num) == float:
            total += num
            
    return total


print(add_all_nums(9, 8, 2.6, 'cinco', 2.7))