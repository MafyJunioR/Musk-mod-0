def generar_excepcion():
    try:
        resultado = 1 / 0
    except Exception as excepcion:
        yield f'Tipo de excepción: {type(excepcion)}'
        yield f'Argumentos de la excepción: {excepcion.args}'
        yield f'Mensaje de error: {str(excepcion)}'
        
        
for expcecion in generar_excepcion():
    print(expcecion)
    
    
print('\n______________________________________\n')
print('\n______________________________________\n')
print('\n______________________________________\n')

class NegativeDifferenceException(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)
    
def restar(a,b):
    if a < b:
        raise NegativeDifferenceException('El resultado es negativo')
    else:
        return a - b
        
try:
    resultado = restar(0,2)
    print(resultado)
except NegativeDifferenceException as negativo:
    print(f'Error: {negativo}')

try:
    resultado = restar(10,2)
    print(resultado)
except NegativeDifferenceException as negativo:
    print(f'Error: {negativo}')
    
    
print('\n______________________________________\n')
print('\n______________________________________\n')
print('\n______________________________________\n')


def dividir(a,b):
    try: 
        if a != int(a) or b != int(b):
            raise TypeError('Error: Los parámetros deben ser numeros enteros.')
        
        resultado = a / b
        return resultado
        
    except ZeroDivisionError:
        return 'Error: El divisor no puede ser 0.'
        
    except TypeError as e:
        return e
        
        
print(dividir(10.2, 2))
print(dividir(10, 0))
print(dividir(10, 5))


print('\n______________________________________\n')
print('\n______________________________________\n')
print('\n______________________________________\n')


def dividir(a,b):
    try: 
        if a != int(a) or b != int(b):
            raise TypeError('Error: Los parámetros deben ser numeros enteros.')
        
        resultado = a / b
        return resultado
        
    except ZeroDivisionError:
        mensaje = 'Error: El divisor no puede ser 0.'
        
    except TypeError as e:
        mensaje = e
    
    finally:
        print('\nLa función ha finalizado correctamente.\n')
        
    return mensaje
print(dividir(10.2, 2))
print(dividir(10, 0))
print(dividir(10, 5))


# No entiendo porque me lo imprime al princio de cada operacion, en vez de imprimirlo al final.