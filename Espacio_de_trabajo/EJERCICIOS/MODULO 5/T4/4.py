import matplotlib.pyplot as plt
import pandas as pd


archivo = r'C:\Users\porcu\Desktop\python\Espacio de trabajo\EJERCICIOS\MODULO 5\Modulo5_company_sales_data-221102-123259.csv'

plt.title('Ventas de pasta de dientes')
plt.xlabel('Numero mes')
plt.ylabel('Numero de unidades vendidas')

numero_mes = pd.read_csv(archivo)['month_number']
pasta_dientes = pd.read_csv(archivo)['toothpaste']

plt.scatter(numero_mes, pasta_dientes, label = 'Ventas de pasta de dientes')
plt.grid(linestyle = '--') # En el ejercicio se pide '-' pero en la foto del mismo sale hecho con '--' ¯\_(ツ)_/¯


plt.legend(loc= 'upper left')
plt.show()