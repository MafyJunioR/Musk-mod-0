'''
Dado dos diccionarios que contienen inventario de dos tiendas diferentes, 
combina los diccionarios en uno solo y maneja posibles productos duplicados 
(suma las cantidades de productos que están en ambas tiendas).

tienda1 = {
    "Laptop": 10,
    "Teléfono": 15,
    "Tablet": 5
}

tienda2 = {
    "Laptop": 7,
    "Impresora": 3,
    "Tablet": 10
}

1. Crea una función llamada `fusionar_inventarios` 
que tome dos diccionarios como parámetros y devuelva un nuevo diccionario fusionado.
2. Llama a la función con `tienda1` y `tienda2`, e imprime el resultado.
'''
def sumar_tiendas(tienda1, tienda2):
    diccionario_fusionado = tienda1.copy()  
    
    for clave, valor in tienda2.items():
        if clave in diccionario_fusionado:
            diccionario_fusionado[clave] += valor
        else:
            diccionario_fusionado[clave] = valor
    
    return diccionario_fusionado  

tienda1 = {
    "Laptop": 10,
    "Teléfono": 15,
    "Tablet": 5
}

tienda2 = {
    "Laptop": 7,
    "Impresora": 3,
    "Tablet": 10
}

tienda_fusionada = sumar_tiendas(tienda1, tienda2)

print(tienda_fusionada)  
