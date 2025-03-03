import matplotlib.pyplot as plt
import pandas as pd


archivo = r'C:\Users\porcu\Desktop\python\Espacio de trabajo\EJERCICIOS\MODULO 5\Modulo5_company_sales_data-221102-123259.csv'

plt.title('Todas las ventas de productos en un stack plot')
plt.xlabel('Numero del mes')
plt.ylabel('Unidades de ventas en numero')

numero_mes = pd.read_csv(archivo)['month_number'] 

y1 = pd.read_csv(archivo)['facecream']                  
y2 = pd.read_csv(archivo)['facewash']                   
y3 = pd.read_csv(archivo)['toothpaste']         
y4 = pd.read_csv(archivo)['bathingsoap']                
y5 = pd.read_csv(archivo)['shampoo']                    
y6 = pd.read_csv(archivo)['moisturizer']                



plt.stackplot(numero_mes,y1,y2,y3,y4,y5,y6, labels=['Crema facial','Lavado de cara','Pasta de dientes', 'Gel de baño','Champú','Moisturizer'], colors= ['red','blue','green','black','orange','yellow'])




plt.legend(loc= 'upper left')
plt.show()