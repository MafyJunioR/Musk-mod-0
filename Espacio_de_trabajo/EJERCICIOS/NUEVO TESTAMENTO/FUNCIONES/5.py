'''Escribe una función llamada check-season,
toma un parámetro de mes y devuelve la temporada: Otoño, Invierno, Primavera o Verano.'''


def check_season(str):
    if str.lower() == 'enero' or str.lower() =='febrero' or str.lower() =='marzo':
        return 'Invierno'
    elif str.lower() == 'abril' or str.lower() =='mayo' or str.lower() =='junio':
        return 'Primavera'
    elif str.lower() == 'julio' or str.lower() =='agosto' or str.lower() =='septiembre':
        return 'Verano'
    elif str.lower() == 'octubre' or str.lower() =='noviembre' or str.lower() =='diciembre':
        return 'Otoño'
    else:
        return 'Escribe bien.'
    
print(check_season('febrero'))
print(check_season('JUNIO'))
print(check_season('JULIO'))
print(check_season('DICieMBRE'))