'''3. **Cuadrados perfectos:**
   Solicita al usuario ingresar un número entero positivo.
   Luego, utiliza un bucle `while` para imprimir los cuadrados perfectos 
   (números que son el resultado de elevar al cuadrado un número entero) hasta llegar al número ingresado.'''
   
   
n = int(input('Ingresa un numero positivo: '))

contador = 1

while contador <= n:
    print(contador**2)
    contador += 1