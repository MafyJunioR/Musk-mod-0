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


def validar_telefono(telefono):
    return len(telefono) == 9 and telefono.isdigit()
    
    
def validar_correo(correo):
    return '@' in correo and correo.endswith('.com')

def agregar_contacto(contactos, nombre, telefono, correo):
    
    errores = []
    
    if nombre in contactos:
        return 'Contacto existente.'
    
    if not validar_telefono(telefono):
        errores.append('\tRevise telefono. (123 456 789).\n')
            
    if not validar_correo(correo):
        errores.append('\tRevise correo. Formato incorrecto. Falta ''@'' y ''.com''. \n')
        
    
    if errores:
        return '\n'.join(errores)
    
    
    
    contactos[nombre] = {
        'telefono' : telefono,
        'correo' : correo
    }
    return 'Contacto agregado.'

def ver_contactos(contactos):
    if not contactos:
        return 'Lista de contactos vacía.'
    else:
        return contactos
    
def buscar_contacto(contactos, nombre):
    if nombre in contactos:
        return contactos[nombre]
    else:
        return 'Contacto no encontrado.'

def borrar_contacto(contactos, nombre):
    if nombre in contactos:
        del contactos[nombre]
        return 'Contacto eliminado.'
    else:
        return 'Contacto no encontrado.'
    
def menu():
    contactos = {}
    while True:
        print('1. Agregar nuevo contacto.')
        print("2. Ver todos los contactos.")
        print("3. Buscar contacto.")
        print("4. Eliminar un contacto.")
        print("5. Salir")
        opcion = input('Seleccione una opción: ')
        
        if opcion == '1':
            nombre = input('NOMBRE: ').lower()
            telefono = input('NUMERO TELEFONICO: ')
            correo = input('CORREO ELECTRONICO: ')
            agenda = agregar_contacto(contactos, nombre, telefono, correo)
            print(agenda)
        
        elif opcion == '2':
            print(ver_contactos(contactos))
            
        elif opcion == '3':
            nombre = input('NOMBRE A BUSCAR: ')
            print(buscar_contacto(contactos, nombre))
            
        elif opcion == '4':
            nombre = input('NOMBRE A ELIMINAR: ')
            print(borrar_contacto(contactos, nombre))
        elif opcion == '5':
            print('Saliendo...')
        else:
            print('Opción no existe.')
            print('')
            
print(menu())