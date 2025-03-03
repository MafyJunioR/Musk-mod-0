import matplotlib.pyplot as plt
import pandas as pd


archivo = r'C:\Users\porcu\Desktop\python\Espacio de trabajo\EJERCICIOS\MODULO 5\Modulo5_company_sales_data-221102-123259.csv'


plt.title('Beneficios por mes')


plt.xlabel('Numero del mes')
numero_mes = pd.read_csv(archivo)['month_number']

plt.ylabel('Beneficio total ')
beneficiostotales = pd.read_csv(archivo)['total_profit']

plt.ylim(100000,500000)

plt.plot(numero_mes,beneficiostotales)




plt.show()