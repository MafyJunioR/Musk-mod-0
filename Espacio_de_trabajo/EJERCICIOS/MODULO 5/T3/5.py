import numpy as np

arrayOne = np.array([[5,6,9],
                     [21,18,27]])

arrayTwo = np.array([[15,33,24],
                    [4,7,1]])

array1plus2 = arrayOne + arrayTwo

print(f'El arrayOne + arrayTwo = \n{array1plus2}')

print(f'Y el cuadrado del resultado anterior es: \n{array1plus2**2}')