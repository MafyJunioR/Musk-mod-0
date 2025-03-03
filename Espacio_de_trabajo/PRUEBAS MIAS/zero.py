'''Enunciado del problema:
Escribe un decorador llamado authenticate que verifique si un usuario está autenticado antes de permitir el acceso a una función.

Si el usuario está autenticado, la función debe ejecutarse normalmente.
Si el usuario no está autenticado, el decorador debe evitar que la función se ejecute e imprimir un mensaje como "Acceso denegado: Usuario no autenticado".
Se aplicará el decorador authenticate a una función llamada view_profile(user), que muestra el perfil de un usuario.

Requisitos:
El decorador authenticate debe aceptar una función que reciba un diccionario de usuario con una clave is_authenticated (un booleano).
Si is_authenticated es True, la función debe ejecutarse.
Si is_authenticated es False, la función no debe ejecutarse y debe imprimir "Acceso denegado: Usuario no autenticado".'''




def authenticate(func):
    def wrapper(user):
        if user.get('is_authenticated'):
            return func(user)
        else:
            print('Acceso denegado: Usuario no autenticado')
    return wrapper


@authenticate
def view_profile(user):
    print(f"Mostrando perfil de {user.get('name', 'Usuario anónimo')}")
    
    
user1 = {'name': 'Carlos', 'is_authenticated':True}
user2 = {'name': 'George', 'is_authenticated':False}

view_profile(user1)
view_profile(user2)