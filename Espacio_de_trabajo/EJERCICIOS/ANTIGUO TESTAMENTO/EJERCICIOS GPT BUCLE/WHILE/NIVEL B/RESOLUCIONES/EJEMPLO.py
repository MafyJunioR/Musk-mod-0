
x = int(input('Ingresa un numero: '))

contador = 0 #iniciamos un contador
# puesto asi va desde el 1 hasta 'x'. aunque el contador empiece en 0
while contador < x:
    contador+= 1 # el numero que pones aqui es igual a
                 # los saltos que da en cada vuelta. 
    print(contador)
    
    

# Puesto asi va desde el 0 hasta 'x-1'.
while contador < x:
    print(contador)
    contador+= 1