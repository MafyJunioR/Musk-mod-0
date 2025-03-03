import pandas as pd

GermanCars = pd.DataFrame({'Company': ['Ford', 'Mercedes', 'BMW', 'Audi'], 'Price': [23845, 171995, 135925, 71400]})
japaneseCars = pd.DataFrame({'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi'], 'Price': [29995, 23600, 61500, 58900]})


resultado_concat = pd.concat([GermanCars, japaneseCars])

resultado_concat_columnas = pd.concat([GermanCars, japaneseCars], axis = 1)

print(resultado_concat)

print('\nCOLUMNAS')
print(resultado_concat_columnas)