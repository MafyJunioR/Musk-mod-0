from datetime import datetime

class Fecha_Hora:
    def __init__(self):
        self.fecha_hora_actual = datetime.now()
        
    def obtener_fecha_hora(self):
        return self.fecha_hora_actual.strftime('\nDia:%d Mes:%m Año:%Y\nHORA: %H:%M:%S\n')
    
    def mostrar_fecha_hora(self):
        print(self.obtener_fecha_hora())
        
    def obtener_año(self):
        return self.fecha_hora_actual.strftime('%Y')
    
    def mostrar_año(self):
        print(f'El año es: {self.obtener_año()}')
        
    def obtener_mes(self):
        return self.fecha_hora_actual.strftime('%m')

    def mostrar_mes(self):
        print(f'El mes es:{self.obtener_mes()}')
        
    def obtener_semana_año(self):
        return self.fecha_hora_actual.isocalendar()[1]
    
    def mostrar_semana_año(self):
        print(f'Es la semana numero {self.obtener_semana_año()} del año.')

    def obtener_dia_semana(self):
        return self.fecha_hora_actual.weekday()
    
    def mostrar_dia_semana(self):
        if self.obtener_dia_semana() == 0:
            print(f'Es el {self.obtener_dia_semana()+1}er dia de la semana.')
        else:
            print(f'Es el {self.obtener_dia_semana()+1}º dia de la semana.')

    def obtener_dia_año(self):
        return self.fecha_hora_actual.timetuple().tm_yday
    
    def mostrar_dia_año(self):
        print(f'Es el dia numero {self.obtener_dia_año()} del año.')
        
    def obtener_dia_mes(self):
        return self.fecha_hora_actual.day
    
    def mostrar_dia_mes(self):
        print(f'Es el dia numero {self.obtener_dia_mes()} de este mes.')
    
fecha_hora = Fecha_Hora()

fecha_hora.mostrar_fecha_hora() #a

fecha_hora.mostrar_año() #b

fecha_hora.mostrar_mes() #c

fecha_hora.mostrar_semana_año() #d

fecha_hora.mostrar_dia_semana() #e / h

fecha_hora.mostrar_dia_año() #f

fecha_hora.mostrar_dia_mes() #g


print('\n______________________________________\n')
print('\n______________________________________\n')
print('\n______________________________________\n')

from datetime import datetime

input_str = 'Jan 1 2014 2:43PM'                     

datetime_object = datetime.strptime(input_str, '%b %d %Y %I:%M%p') #He tenido que buscar en google para que sirve cada '%', es la primera vez que trabajo con ello

output_str = datetime_object.strftime('%Y-%m-%d %H:%M:%S')

print(f'OUTPUT: {output_str}')

print('\n______________________________________\n')
print('\n______________________________________\n')
print('\n______________________________________\n')

from datetime import datetime

hora_actual = datetime.now().strftime('%H:%M:%S')

print(hora_actual)

print('\n______________________________________\n')
print('\n______________________________________\n')
print('\n______________________________________\n')

from datetime import datetime, timedelta


fecha_actual = datetime.now()

fecha_resultante = fecha_actual - timedelta(days=5)

print(fecha_resultante.strftime('%d %m %Y'))

print('\n______________________________________\n')
print('\n______________________________________\n')
print('\n______________________________________\n')

from datetime import datetime

marca_unix = 1284105682

fecha_legible = datetime.fromtimestamp(marca_unix) # ó directamente escribir la marca unix entre los parentesis, sin crear la variable anterior

print(fecha_legible)

print('\n______________________________________\n')
print('\n______________________________________\n')
print('\n______________________________________\n')

from datetime import datetime, timedelta

hora_actual = datetime.now()

hora_resultante = hora_actual + timedelta(seconds=5)

print(hora_actual)

print('\n______________________________________\n')
print('\n______________________________________\n')
print('\n______________________________________\n')

from datetime import datetime

fecha_actual = datetime.now()

numero_semana = fecha_actual.isocalendar()[1]

print(f'El numero de la semana es: {numero_semana}')


print('\n______________________________________\n')
print('\n______________________________________\n')
print('\n______________________________________\n')


from datetime import date, timedelta

def obtener_domingos(year):
    
    fecha = date(year, 1, 1)
    
    while fecha.weekday() != 6:
        fecha += timedelta(days=1)
        
    domingos = []
    
    while fecha.year == year:
        domingos.append(fecha)
        fecha += timedelta(days=7)
        
    return domingos

year = 2024
domingos = obtener_domingos(year)

for domingo in domingos:
    print(domingo)
    
print('\n______________________________________\n')
print('\n______________________________________\n')
print('\n______________________________________\n')


from datetime import date

def contar_lunes_primer_dia_mes(start_year, end_year):
    contador_lunes = 0
    
    for year in range(start_year,end_year+1):
        for month in range(1,13):
            primer_dia = date(year,month,1)
            if primer_dia.weekday() == 0:
                contador_lunes += 1
                
    return contador_lunes


start_year = 2015
end_year = 2016

numero_lunes = contar_lunes_primer_dia_mes(start_year,end_year)

print(numero_lunes)


print('\n______________________________________\n')
print('\n______________________________________\n')
print('\n______________________________________\n')

from datetime import datetime,timedelta


input_str = '2 2 2024' 

fecha_especifica = datetime.strptime(input_str, '%d %m %Y')

fechas = []

for i in range(12):
    nueva_fecha = fecha_especifica + timedelta(days=i * 20)
    fechas.append(nueva_fecha)
    
for fecha in fechas:
    print(fecha.strftime('%d %m %Y'))