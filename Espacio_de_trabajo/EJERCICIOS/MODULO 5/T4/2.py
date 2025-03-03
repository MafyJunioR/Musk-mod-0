import matplotlib.pyplot as plt
import pandas as pd


archivo = r'C:\Users\porcu\Desktop\python\Espacio de trabajo\EJERCICIOS\MODULO 5\Modulo5_company_sales_data-221102-123259.csv'


plt.title('Beneficios por mes')


plt.xlabel('Numero del mes')
numero_mes = pd.read_csv(archivo)['month_number']

plt.ylabel('Numero de unidades vendidas ')
unidadesvendidas = pd.read_csv(archivo)['total_units']

plt.plot(numero_mes, unidadesvendidas, marker = 'o' ,color= 'red', linestyle = '--', linewidth = '3', label = 'Profit data of last year', markerfacecolor = 'black') # He buscado los argumentos de personalizacion en google, obviamente.
plt.legend(loc = 'lower right')


plt.show()
