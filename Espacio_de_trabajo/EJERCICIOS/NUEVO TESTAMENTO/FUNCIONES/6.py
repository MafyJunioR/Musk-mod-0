'''6.Escribe una función llamada calcular_pendiente
que devuelva la pendiente de una ecuación lineal.'''


def calcular_pendiente(y, x):
    primera = y * y - y
    segunda = x ** 2 - x
    m = primera / segunda
    
    return m


calcular_pendiente(9,8)