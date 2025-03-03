'''
Descripción:
Crearás una aplicación de consola que permitirá al usuario agregar, ver, buscar y eliminar contactos.
Cada contacto tendrá un nombre, un número de teléfono y un correo electrónico.

Funcionalidades:
Agregar un nuevo contacto.
Ver todos los contactos.
Buscar un contacto por nombre.
Eliminar un contacto.
Salir de la aplicación.

Estructura del Proyecto:
Función principal: Inicia la aplicación y muestra el menú principal.
Funciones para cada operación: Agregar, ver, buscar y eliminar contactos.'''

contactos = {}
correos = {}


# MENÚ

while True:
    print('____________________________________________________')
    menu = int(input('''                    MENÚ
                     1.Agregar nuevo contacto.
                     2.Ver todos los contactos.
                     3.Buscar contacto.
                     4.Eliminar un contacto.
                     5.Salir
----------------------------------------------------
                    '''))
    
    
    if menu == 1:
        
        nombre = input('NOMBRE: ')
# Funcion para agregar contactos.
        while True:    
                numero = (input('NUMERO TELEFONICO: '))
                if len(numero) != 9 or not numero.isdigit():
                    print('____________________________________________________')
                    print('Revisa el numero ingresado.')
                    print('----------------------------------------------------')
                else:
                    if nombre.lower() not in contactos:
                        contactos[nombre.lower()] = []
                    contactos[nombre.lower()].append(numero)
                    break
            
            
        while True:
                correo = input('CORREO ELECTRONICO: ')
                if '@' not in correo or not correo.endswith('.com'):
                    print('Revise correo. Falta ''@'' y acabar en ''.com'' ')
                else:
                    if nombre.lower() not in correos:
                        correos[nombre.lower()] = []
                    correos[nombre.lower()].append(correo)
                    print('Contacto agregado con éxito')
                    print('____________________________________________________')
                    print('----------------------------------------------------')
                    break
                
                
    
    elif menu == 2:
        
        while True:
            print('____________________________________________________')
            print(contactos)
            print(correos)
            print('----------------------------------------------------')
            break
            
            
    elif menu == 3:
        
        while True:
            quien = input('BUSCAR: ').lower()
            
            if quien in contactos:
                print('____________________________________________________')
                print(f'''                          {quien}
                        {contactos[quien]}
                        {correos[quien]}''')
                print('----------------------------------------------------')
                break
            else:
                print('____________________________________________________')
                print('Nombre no encontrado en la agenda.')
                print('----------------------------------------------------')
                break
            
    elif menu == 4:
        
        
        borrar = input('ELIMINAR: ').lower()
            
        if borrar in contactos:
            del contactos[borrar]
            del correos[borrar]
            print('Contacto eliminado')
        else:
                
            print('____________________________________________________')
            print('Contacto no encontrado.')
            print('----------------------------------------------------')
    elif menu == 5:
        
        print('____________________________________________________')
        print('Saliendo.')
        print('----------------------------------------------------')
        break
    
    else:
        
        print('____________________________________________________')
        print('No existe esa opción...')
        print('----------------------------------------------------')