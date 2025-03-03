'''### Ejercicio 6: Patrón de Números
Escribe un programa que tome un número entero `n` como entrada del usuario y utilice un bucle para imprimir un patrón de números en forma de triángulo. 
Por ejemplo, si el usuario ingresa 5, la salida podría verse así:

1
22
333
4444
55555

'''

n = int(input('Ingresa un numero y te ''dibujo'' un triangulo: '))

triangulo = 1

for i in range(1, n+1):
    print(str(i) * i)