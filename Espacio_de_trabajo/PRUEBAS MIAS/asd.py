def prod(l1, l2):
    solution = []  # Lista para almacenar los resultados
    
    # Generador interno que produce la multiplicación de los elementos
    def generador():
        for i in range(min(len(l1), len(l2))):
            yield l1[i] * l2[i]
    
    gen = generador()  # Crear el generador

    # Intentar obtener elementos hasta que se produzca StopIteration
    try:
        while True:
            solution.append(next(gen))  # Agregar el siguiente elemento a la lista
    except StopIteration:
        pass  # Capturar la excepción cuando se termina la iteración
    
    return solution  # Devolver la lista completa

# Ejemplo de uso
l1 = list(range(1, 11))
l2 = list(range(1, 11))
resultado = prod(l1, l2)
print(resultado)  # Salida: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]