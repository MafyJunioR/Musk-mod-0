'''**Comparación de cadenas:**
   Pide al usuario que ingrese dos cadenas y verifica si son iguales. 
   Muestra un mensaje indicando si son iguales o diferentes.'''
   
cadena1 = (input('Ingresa un texto: '))
cadena2 = (input('Ingresa el mismo texto haciendo memoria: '))


if cadena1.lower() == cadena2.lower():
    print('No hay diferencia')
elif cadena1 != cadena2:
    print('Son distintos')