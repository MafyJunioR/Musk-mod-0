'App bancaria: Simula depósitos, retiros y saldos en una aplicación básica.'

def mostrar_saldo(saldo):
    print(f'Tu saldo es de : {saldo:.2f} €')

def depositar():
    monto = float(input('Cuanto dinero quiere ingresar?'))
    if monto < 0:
        print(f'La tiene que ser mayor que 0€.')
        return 0
    else:
        return monto
    
def retirar(saldo):
    monto = float(input('Cuanto dinero quiere retirar?'))
    if monto > saldo:
        print(f'No dispone suficiente saldo. Debe retirar {saldo} o menos.')
        return 0
    elif monto < 0:
        print(f'La cantidad a retirar debe ser mayor que 0.')
        return 0
    else:
        return monto

def menu_principal():
    saldo = 0
    
    while True:
    
        opcion = int(input('\n\t\tMenú:\n\t1.Mostrar saldo.\n\t2.Depositar.\n\t3.Retirar.\n\t4.Salir.\n\t\t'))
    
        if opcion == 1:
            mostrar_saldo(saldo)
        elif opcion == 2:
            saldo += depositar()
        elif opcion == 3:
            saldo -= retirar(saldo)
        elif opcion == 4:
            break
        else:
            print('\nElija una opción del 1 al 4.')
            
menu_principal()