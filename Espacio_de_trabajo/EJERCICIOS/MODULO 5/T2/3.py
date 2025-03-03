import pandas as pd

archivo = r'C:\Users\porcu\Desktop\python\Espacio de trabajo\EJERCICIOS\MODULO 5\Modulo5_Automobile_data-221102-123259.csv'
datos = pd.read_csv(archivo)

fila_mas_cara = datos.loc[datos['price'].idxmax()]

empresa = fila_mas_cara['company']
precio = fila_mas_cara['price']

print(f'La empresa con el coche mas caro es: {empresa} y su coche vale: {precio:.2f} €')