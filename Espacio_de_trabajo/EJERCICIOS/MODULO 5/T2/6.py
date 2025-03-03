import pandas as pd

archivo = r'C:\Users\porcu\Desktop\python\Espacio de trabajo\EJERCICIOS\MODULO 5\Modulo5_Automobile_data-221102-123259.csv'
datos = pd.read_csv(archivo)

coche_mas_caro_de_cada_empresa = datos.loc[datos.groupby('company')['price'].idxmax()]

print(f'El coche mas caro de cada empresa es: {coche_mas_caro_de_cada_empresa}')