import pandas as pd

archivo = r'C:\Users\porcu\Desktop\python\Espacio de trabajo\EJERCICIOS\MODULO 5\Modulo5_Automobile_data-221102-123259.csv'
datos = pd.read_csv(archivo)

print(f'Las primeras 5 filas:\n{datos.head()}')

print(f'Las ultimas 5 filas:\n{datos.tail()}')