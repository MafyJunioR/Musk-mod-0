'''3. Haz un programa que devuelva múltiples valores desde una función.
Crea la función calculaion() de modo que pueda aceptar dos variables y calcular sumas y restas.
Además, debe devolver tanto la suma como la resta en una sola llamada.'''


def calculaion(a,b):
    def resta():
        c = a - b
        return c
    
    def suma():
        c = a + b
        return c
    
    return resta(), suma()

print(calculaion(9,8))