import numpy as np


matriz8x3 = np.arange(10, 34).reshape(8, 3)

submatrices = [
    matriz8x3[:4, :2],
    matriz8x3[:4, 2:],
    matriz8x3[4:, :2],
    matriz8x3[4:, 2:]
]

print(matriz8x3,'\n_____\n',submatrices)