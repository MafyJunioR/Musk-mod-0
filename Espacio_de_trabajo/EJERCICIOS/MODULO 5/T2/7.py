import pandas as pd

archivo = r'C:\Users\porcu\Desktop\python\Espacio de trabajo\EJERCICIOS\MODULO 5\Modulo5_Automobile_data-221102-123259.csv'
datos = pd.read_csv(archivo)

km_medio = datos.groupby('company')['average-mileage'].median()

print(f'El kilometraje medio de cada empresa es:\n\n{km_medio}')