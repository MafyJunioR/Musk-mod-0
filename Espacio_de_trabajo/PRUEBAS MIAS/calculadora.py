def calcular(operador, num1, num2):
    if operador == '+':
        return num1 + num2
    elif operador == '-':
        return num1 - num2
    elif operador == '/':
        if num2 == 0:
            raise ValueError('No se puede dividir entre cero.')
        return num1 / num2
    elif operador == '*':
        return num1 * num2
    else:
        raise ValueError (f'{operador} no válido.')
        
        
def main():
    print('Calculadora python.')

    try:
        operador = input('Introduce un operador (+ - * /)').strip()
        operadores_validos = ['+', '-', '*', '/']
        if operador not in operadores_validos:
            print(f'{operador} no válido.')
            return
        
        num1 = float(input('Introduce el primer numero.'))
        num2 = float(input('Introduce el segundo numero.'))
        
        resultado = calcular(operador, num1, num2)
        print(f'El resultado es: {round(resultado, 3)}')
        
    except ValueError as e:
        print(f'Error: {e}')
        
main()