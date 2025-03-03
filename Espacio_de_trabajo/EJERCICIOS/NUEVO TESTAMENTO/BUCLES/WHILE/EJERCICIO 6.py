'''
Ejercicio 6: Invertir un número
Escribe un programa que pida al usuario un número entero positivo 
y luego invierta el número usando un bucle `while`. Por ejemplo, si el usuario ingresa `12345`, el programa debe mostrar `54321`.
'''



numero = int(input("Ingresa un número entero positivo: "))
numero_invertido = 0
while numero > 0:
    digito = numero % 10
    numero_invertido = numero_invertido * 10 + digito
    numero //= 10
print(f'El número invertido es: {numero_invertido}')


'''Estado Inicial:
numero = 12345
numero_invertido = 0
Iteración 1:
digito = numero % 10 → digito = 12345 % 10 → digito = 5
numero_invertido = numero_invertido * 10 + digito → numero_invertido = 0 * 10 + 5 → numero_invertido = 5
numero = numero // 10 → numero = 12345 // 10 → numero = 1234
Estado después de la Iteración 1:

numero = 1234
numero_invertido = 5
Iteración 2:
digito = numero % 10 → digito = 1234 % 10 → digito = 4
numero_invertido = numero_invertido * 10 + digito → numero_invertido = 5 * 10 + 4 → numero_invertido = 54
numero = numero // 10 → numero = 1234 // 10 → numero = 123
Estado después de la Iteración 2:

numero = 123
numero_invertido = 54
Iteración 3:
digito = numero % 10 → digito = 123 % 10 → digito = 3
numero_invertido = numero_invertido * 10 + digito → numero_invertido = 54 * 10 + 3 → numero_invertido = 543
numero = numero // 10 → numero = 123 // 10 → numero = 12
Estado después de la Iteración 3:

numero = 12
numero_invertido = 543
Iteración 4:
digito = numero % 10 → digito = 12 % 10 → digito = 2
numero_invertido = numero_invertido * 10 + digito → numero_invertido = 543 * 10 + 2 → numero_invertido = 5432
numero = numero // 10 → numero = 12 // 10 → numero = 1
Estado después de la Iteración 4:

numero = 1
numero_invertido = 5432
Iteración 5:
digito = numero % 10 → digito = 1 % 10 → digito = 1
numero_invertido = numero_invertido * 10 + digito → numero_invertido = 5432 * 10 + 1 → numero_invertido = 54321
numero = numero // 10 → numero = 1 // 10 → numero = 0
Estado después de la Iteración 5:

numero = 0
numero_invertido = 54321
Fin del Bucle:
El bucle while termina porque numero ya no es mayor que 0.

Resultado Final:
El número invertido es: 54321'''