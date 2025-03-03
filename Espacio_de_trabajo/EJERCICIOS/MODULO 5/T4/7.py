import matplotlib.pyplot as plt
import pandas as pd

archivo = r'C:\Users\porcu\Desktop\python\Espacio de trabajo\EJERCICIOS\MODULO 5\Modulo5_company_sales_data-221102-123259.csv'

plt.title('Profit')
plt.xlabel('Profit en dolares')
plt.ylabel('Actual profit en dolares')

beneficiototal = pd.read_csv(archivo)['total_profit']

plt.hist(beneficiototal, label= 'Profit')

plt.legend(loc = 'upper left')
plt.show()