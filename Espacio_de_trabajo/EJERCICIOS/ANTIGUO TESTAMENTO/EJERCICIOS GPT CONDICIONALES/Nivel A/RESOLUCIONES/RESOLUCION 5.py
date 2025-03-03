'''**Verificación de edad:**
   Solicita al usuario que ingrese su edad
   y verifica si es mayor de edad (18 años o más) o menor de edad.'''
   

edad = int(input('Inresa tu edad: '))

if edad < 18:
    print(f'Tienes {edad} años. Eres menor de edad')
else:
    print(f'Tienes {edad} años. Eres mayor de edad')