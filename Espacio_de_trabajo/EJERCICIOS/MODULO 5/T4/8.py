import matplotlib.pyplot as plt
import pandas as pd

archivo = r'Espacio_de_trabajo\EJERCICIOS\MODULO 5\Modulo5_company_sales_data-221102-123259.csv'

plt.title('Sales data')
plt.xlabel('Profit en dolares')
plt.ylabel('Actual profit en dolares')

pastadientes = pd.read_csv(archivo)['toothpaste'].sum()
lavadocara = pd.read_csv(archivo)['facewash'].sum()
moisturizer = pd.read_csv(archivo)['moisturizer'].sum()
gelbaño = pd.read_csv(archivo)['bathingsoap'].sum()
shampoo = pd.read_csv(archivo)['shampoo'].sum()
cremafacial = pd.read_csv(archivo)['facecream'].sum()    #Sumamos los datos de cada producto


x = [pastadientes,lavadocara,moisturizer,gelbaño,shampoo,cremafacial]
etiquetas = ['Pasta de dientes', 'Lavado de cara', 'Moisturizer', 'Gel de baño', 'Shampoo', 'Crema facial']

plt.pie(x, labels= etiquetas, autopct= '%1.1f%%')

plt.show()