import matplotlib.pyplot as plt
import pandas as pd

archivo = r'C:\Users\porcu\Desktop\python\Espacio de trabajo\EJERCICIOS\MODULO 5\Modulo5_company_sales_data-221102-123259.csv'

plt.title('Facewash and facecream sales data')
plt.xlabel('Numero del mes')
plt.ylabel('Unidades de venta en numero')

numero_mes = pd.read_csv(archivo)['month_number'] # X

y1 = pd.read_csv(archivo)['facecream']              # Los distintos ejes Y para las barras
y2 = pd.read_csv(archivo)['facewash']               #

ancho = 0.2 #damos separación 

plt.bar(numero_mes - ancho/2 ,y1, width = 0.2, label = 'Ventas crema facial', color = 'blue') #situamos las barras mas a la izquiera ' -ancho/2 '
plt.bar(numero_mes + ancho/2 ,y2, width = 0.2, label = 'Ventas lavado de cara', color = 'orange' ) # y estas al contrario ' +ancho/2 '                   Entre 2 para que quede parejo al ancho que hemos dado antes 
plt.grid(linestyle = '--')

plt.legend(loc= 'upper left')
plt.show()