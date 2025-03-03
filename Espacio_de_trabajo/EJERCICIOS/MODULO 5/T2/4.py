import pandas as pd

archivo = r'C:\Users\porcu\Desktop\python\Espacio de trabajo\EJERCICIOS\MODULO 5\Modulo5_Automobile_data-221102-123259.csv'
datos = pd.read_csv(archivo)

filas_toyota = datos.loc[datos['company'] == 'toyota']
print(filas_toyota)