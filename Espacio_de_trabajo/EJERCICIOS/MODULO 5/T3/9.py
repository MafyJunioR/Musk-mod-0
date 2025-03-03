import numpy as np

sampleArray = np.array([[34, 43, 73],
                        [82, 22, 12],
                        [53, 94, 66]])

newcolumn = np.array([[10, 10, 10]])

columnahueco = np.delete(sampleArray,1, axis= 1)
columnas_juntas = np.insert(columnahueco, 1, newcolumn,axis=1)

print(columnas_juntas)