import matplotlib.pyplot as plt
import pandas as pd


archivo = r'C:\Users\porcu\Desktop\python\Espacio de trabajo\EJERCICIOS\MODULO 5\Modulo5_company_sales_data-221102-123259.csv'

plt.title('Ventas')
plt.xlabel('Numero mes')
plt.ylabel('Unidades de ventas en numero')


numero_mes = pd.read_csv(archivo)['month_number'] # X

y1 = pd.read_csv(archivo)['facecream']                  #
y2 = pd.read_csv(archivo)['facewash']                   #
y3 = pd.read_csv(archivo)['toothpaste']         # Los diferentes ejes Y
y4 = pd.read_csv(archivo)['bathingsoap']                #
y5 = pd.read_csv(archivo)['shampoo']                    #
y6 = pd.read_csv(archivo)['moisturizer']                #



# Pongo los colores de cada elemento segun el propio python me los enseña en el archivo .csv
plt.plot(numero_mes, y1, color = 'blue', marker = 'o', linewidth = '3', label = 'Facecream')
plt.plot(numero_mes, y2, color = 'yellow', marker = 'o', linewidth = '6', label = 'Facewash') #Facewash y moisturizer tienen los mismos datos, le doy mas anchura a la linea.
plt.plot(numero_mes, y3, color = 'darkgreen', marker = 'o', linewidth = '3', label = 'Toothpaste')
plt.plot(numero_mes, y4, color = 'red', marker = 'o', linewidth = '3', label = 'Bathingsoap')
plt.plot(numero_mes, y5, color = 'cyan', marker = 'o', linewidth = '3', label = 'Shampoo')
plt.plot(numero_mes, y6, color = 'lightgreen', marker = 'o', linewidth = '3', label = 'Moisturizer')




plt.legend(loc= 'upper left') # Ubico la leyenda
plt.show()