import numpy as np

sampleArray = np.array([[34, 43, 73],
                        [82, 22, 12],
                        [53, 94, 66]])


ordenadofila = np.sort(sampleArray, axis=1)
ordenadocolumna = np.sort(sampleArray, axis=0)

print(ordenadocolumna)
print(ordenadofila)