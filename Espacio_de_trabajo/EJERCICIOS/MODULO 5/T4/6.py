import matplotlib.pyplot as plt
import pandas as pd

archivo = r'C:\Users\porcu\Desktop\python\Espacio de trabajo\EJERCICIOS\MODULO 5\Modulo5_company_sales_data-221102-123259.csv'

plt.title('Ventas de jabon de baño')
plt.xlabel('Numero del mes')
plt.ylabel('Unidades de venta en numero')

numero_mes = pd.read_csv(archivo)['month_number']

jabonbaño = pd.read_csv(archivo)['bathingsoap']

plt.bar(numero_mes, jabonbaño, width = 0.5)
plt.grid(linestyle = '--')

plt.show()

#Guardamos
plt.savefig('Grafico ventas baño.png')
plt.close()