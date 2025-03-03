'''2. **Día de la semana:**
   Pide al usuario que ingrese un número del 1 al 7
   y muestra el día de la semana correspondiente
   (1 para lunes, 2 para martes, etc.).'''
   
numero = int(input('Ingresa un numero para saber que dia de la semana corresponde: '))

if numero == 1:
    print('Es lunes')
elif numero == 2:
    print('Es martes')
elif numero == 3:
    print('Es miercoles')
elif numero == 4:
    print('Es jueves')
elif numero == 5:
    print('Es viernes')
elif numero == 6:
    print('Es sabado')
elif numero == 7:
    print('Es domingo')
else:
    print('Ingresa un numero del 1 al 7')