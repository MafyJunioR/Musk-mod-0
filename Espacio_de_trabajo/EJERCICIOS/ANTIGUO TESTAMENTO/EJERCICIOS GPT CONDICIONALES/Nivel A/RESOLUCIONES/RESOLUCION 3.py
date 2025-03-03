'''3. **Calculadora simple:**
Crea un programa que solicite dos números y una operación 
(+, -, *, /) al usuario. Luego, realiza la operación y muestra el resultado.'''

numero1 = float(input('Ingresa un numero: '))
operacion = (input('Ingresa un simbolo (+, -, *, /): '))
numero2 = float(input('Ingresa otro numero: '))

if operacion == '+':
    print(numero1 + numero2)
elif operacion == '-':
    print(numero1 - numero2)
elif operacion == '*':
    print(numero1 * numero2)
elif operacion == '/':
    print(numero1 / numero2)
else:
    print('UwU')
    

#MEJORABLE notablemente