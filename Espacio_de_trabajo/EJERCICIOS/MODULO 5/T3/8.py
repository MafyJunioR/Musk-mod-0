import numpy as np

sampleArray = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])

print(np.max(sampleArray, axis=0))
print(np.min(sampleArray,axis=1))


