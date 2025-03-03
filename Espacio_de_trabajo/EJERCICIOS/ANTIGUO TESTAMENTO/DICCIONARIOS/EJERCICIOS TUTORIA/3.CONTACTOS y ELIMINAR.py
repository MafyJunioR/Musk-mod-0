'''Diccionario de Contactos: Crea un diccionario de contactos
con nombres como claves y números de teléfono como valores.

Eliminar Elemento: Elimina un elemento específico de un 
diccionario y verifica si la clave existe antes de eliminar.'''


contactos={
    'Sergio': '654321987',
    'Bárbara':'693582471',
    'Jorge':'687587398',
}

clave_para_eliminar = input('Ingresa un nombre que quieras eliminar de la lista de contactos: ')

if clave_para_eliminar in contactos:
    numero_eliminado = contactos.pop(clave_para_eliminar)
    print(f'Se ha eliminado a {clave_para_eliminar}. Tenia este numero: {numero_eliminado}')
else:
    print(f'El nombre ingresado no existe')
    
print(f'Los contactos que quedan son: {contactos}')