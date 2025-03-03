import pandas as pd

archivo = r'C:\Users\porcu\Desktop\python\Espacio de trabajo\EJERCICIOS\MODULO 5\Modulo5_Automobile_data-221102-123259.csv'
datos = pd.read_csv(archivo)

empresas = datos['company']

lista = {}
for empresa in empresas:
    if empresa in lista:
        lista[empresa] += 1
    elif empresa not in lista:
        lista[empresa] = 1
print(lista)