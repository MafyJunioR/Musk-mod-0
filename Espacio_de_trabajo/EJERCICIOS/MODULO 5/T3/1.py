import numpy as np


nparray = np.array([[1,2],
                    [3,4],
                    [5,6],
                    [7,8]])


shape = nparray.shape
dimensiones = nparray.ndim
tamanno_cada_elemento_bytes = nparray.itemsize

print(f'Shape: {shape}\nDimensiones: {dimensiones}\nTamaño en bytes: {tamanno_cada_elemento_bytes}')