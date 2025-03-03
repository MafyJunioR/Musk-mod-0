# Crear un diccionario vacío
diccionario = {}

# Agregar elementos
diccionario['nombre'] = 'Juan'
diccionario['edad'] = 20
diccionario['carrera'] = 'Informática'

# Obtener un valor
print(diccionario.get('nombre'))  # Salida: Juan

# Eliminar un elemento y obtener su valor
edad = diccionario.pop('edad')
print(edad)  # Salida: 20

# Obtener todas las claves
print(diccionario.keys())  # Salida: dict_keys(['nombre', 'carrera'])

# Obtener todos los valores
print(diccionario.values())  # Salida: dict_values(['Juan', 'Informática'])

# Obtener todos los pares clave-valor
print(diccionario.items())  # Salida: dict_items([('nombre', 'Juan'), ('carrera', 'Informática')])

# Verificar si una clave existe
print('nombre' in diccionario)  # Salida: True

# Actualizar el diccionario
diccionario.update({'edad': 21, 'universidad': 'MIT'})
print(diccionario)  # Salida: {'nombre': 'Juan', 'carrera': 'Informática', 'edad': 21, 'universidad': 'MIT'}

# Copiar el diccionario
copia_diccionario = diccionario.copy()
print(copia_diccionario)  # Salida: {'nombre': 'Juan', 'carrera': 'Informática', 'edad': 21, 'universidad': 'MIT'}

# Eliminar todos los elementos
diccionario.clear()
print(diccionario)  # Salida: {}
