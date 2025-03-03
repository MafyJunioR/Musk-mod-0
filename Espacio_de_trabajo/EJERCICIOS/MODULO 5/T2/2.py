import pandas as pd

archivo = r'C:\Users\porcu\Desktop\python\Espacio de trabajo\EJERCICIOS\MODULO 5\Modulo5_Automobile_data-221102-123259.csv'
datos = pd.read_csv(archivo)

# VER QUE TIENE EL CONJUNTO DE DATOS, DE UNA FORMA GENERAL
print(f'\nLas 5 primeras filas\n\n{datos.head()}')
print(f'\nINFORMACIÓN\n\n{datos.info()}')
print(f'\nDESCRIPCIÓN\n\n{datos.describe()}')


# REEMPLAZO COLUMNAS CON VALORES NULOS POR UN VALOR FIJO ('DESCONOCIDO')

valores_a_reemplazar = ['?', 'n.a', 'NaN']
datos = datos.replace(valores_a_reemplazar, None)

# ACTUALIZO
datos.to_csv(archivo, index=False)

# VUELVO A MIRAR EL ARCHIVO PARA CONFIRMAR CAMBIOS
print(f'\n-------------------------\n-------------------------\n-------------------------\n')
print(f'\nLas 5 primeras filas\n\n{datos.head()}')
print(f'\nINFORMACIÓN\n\n{datos.info()}')
print(f'\nDESCRIPCIÓN\n\n{datos.describe()}')
