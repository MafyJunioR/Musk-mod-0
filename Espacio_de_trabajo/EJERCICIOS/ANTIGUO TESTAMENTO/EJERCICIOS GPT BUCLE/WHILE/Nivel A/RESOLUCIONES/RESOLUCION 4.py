'''4. **Suma hasta un límite:**
   Solicita al usuario ingresar un límite superior. Utiliza un bucle `while` para calcular la suma de los números del 1 al límite ingresado.'''
   

n = int(input('Ingresa un numero: '))

suma = 0
contador = 1

while contador <= n:
    suma += contador
    contador += 1
    
print(f'La suma de los numores del 1 al {n} es: {suma}')