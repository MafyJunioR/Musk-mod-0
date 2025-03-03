import matplotlib.pyplot as plt
import pandas as pd


archivo = r'C:\Users\porcu\Desktop\python\Espacio de trabajo\EJERCICIOS\MODULO 5\Modulo5_company_sales_data-221102-123259.csv'
plt.xlabel('Numero mes')
plt.ylabel('Unidades de ventas en numero')

numero_mes = pd.read_csv(archivo)['month_number']
y1 =pd.read_csv(archivo)['bathingsoap']

plt.subplot(2,1, 1)
plt.plot(numero_mes, y1, color = 'black', marker = 'o', linewidth = 3)
plt.title('Ventas gel de baño')


y2= pd.read_csv(archivo)['facewash']

plt.subplot(2,1, 2)
plt.plot(numero_mes, y2, color = 'red', marker = 'o', linewidth = '3')
plt.title('Ventas lavado de cara')

plt.show()