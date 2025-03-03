# Pon lo que ganas y lo que gastas mensualmente y el programa te dirá como ahorrar (o no, XD)



ingreso_mensual = int(input('Cuanto ganas al mes?: '))
gasto_mensual = int(input('Cuanto gastas al mes?: '))
restante = ingreso_mensual - gasto_mensual
SMI = 1080

if ingreso_mensual <= SMI:
    print('944 020 099, es el numero de telefono de Caritas, te hace falta')
    
elif ingreso_mensual > 1080 and ingreso_mensual <= 1500:
    if restante <= 0 or restante < 100:
        print('Algo no cuadra, estás gastando mucho pa´')
    elif restante >= 100 and restante < 400:
        print('¿Por qué gastas tanto?')
    elif restante >= 400 and restante < 900:
        print('Ahorras bastante')
        
elif ingreso_mensual > 1500 and ingreso_mensual <= 1700:
    if restante <= 0 or restante < 400:
        print('¿Has llenado el depósito o qué?')
    elif restante >= 400 and restante < 700:
        print('Tu puedes')
    elif restante >= 700 and restante <= 1000:
        print('Muy bien')
    elif restante > 1000:
        print('COJONUDO, no sé como lo has hecho pero muy bien')
        
elif ingreso_mensual > 1700 and ingreso_mensual <= 2500:
    if restante <= 0 or restante <= 800:
        print('No sé cómo lo haces pero sigues gastando como un burro')
    elif restante > 800 and restante <= 1700:
        print('Vas por buen camino')
    elif restante > 1700 and restante <= 2500:
        print('DE PUTA MADRE, espero que hayas pagado las facturas')
        
elif ingreso_mensual > 2500:
    if restante <= 0 or restante <= 500:
        print('Cuidadito, que como viene asi se va')
    elif restante > 500 and restante < 1000:
        print('Buena vida te estas gastando')
    elif restante >= 1000 and restante <= 2500:
        print('No seas tacaño y paga tu la ronda')
else:
    print('Ingresa datos')
    

print(restante)