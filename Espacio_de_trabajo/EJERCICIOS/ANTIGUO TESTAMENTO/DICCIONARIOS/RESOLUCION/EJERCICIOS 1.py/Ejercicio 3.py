'''
Supongamos que tienes un diccionario llamado `productos`
que contiene nombres de productos y sus precios. Crea el siguiente diccionario para empezar:

productos = {
    "Manzana": 1.2,
    "Banana": 0.8,
    "Naranja": 0.9,
    "Mango": 1.5,
}

1. Agrega un nuevo producto al diccionario.
2. Cambia el precio de la "Banana" a 0.85.
3. Elimina el producto "Naranja".
4. Imprime todos los productos con sus precios.
5. Imprime solo los nombres de todos los productos.
6. Imprime solo los precios de todos los productos.
'''

productos = {
    "Manzana": 1.2,
    "Banana": 0.8,
    "Naranja": 0.9,
    "Mango": 1.5,
}

productos.update({
    'Higo': '2.5',
    'Banana': '0.85'
})

productos.pop('Naranja')
print(productos)

nombres = productos.keys()
precios = productos.values()

print(f'Nombres de productos:', list(nombres))
print(f'Precios de productos:', list(precios))

