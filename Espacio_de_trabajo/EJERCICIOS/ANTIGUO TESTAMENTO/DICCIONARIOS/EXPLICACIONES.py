'Acceder a elementos: Puedes acceder a los valores asociados a una clave específica utilizando la sintaxis de corchetes [].'
mi_diccionario = {"clave1": "valor1", "clave2": "valor2"}
print(mi_diccionario["clave1"])  # Imprime "valor1"




'Agregar elementos: Puedes agregar nuevas parejas clave-valor a un diccionario.'
mi_diccionario["clave3"] = "valor3"




'Eliminar elementos: Puedes eliminar una pareja clave-valor de un diccionario utilizando la palabra clave del.'
del mi_diccionario["clave2"]




'Iterar sobre claves: Puedes iterar sobre las claves de un diccionario utilizando un bucle for.'
for clave in mi_diccionario:
    print(clave)
    
    
    
    
'Iterar sobre valores: Puedes iterar sobre los valores de un diccionario utilizando el método values().'
for valor in mi_diccionario.values():
    print(valor)
    
 
 
    
'Iterar sobre pares clave-valor: Puedes iterar sobre las parejas clave-valor de un diccionario utilizando el método items().'
for clave, valor in mi_diccionario.items():
    print(clave, valor)
    
  
  
    
'Comprobar si una clave está presente: Puedes verificar si una clave está presente en un diccionario utilizando el operador in.'
if "clave1" in mi_diccionario:
    print("La clave está presente")
    
    
    
'Longitud del diccionario: Puedes obtener la cantidad de elementos en un diccionario utilizando la función len().'
print(len(mi_diccionario))