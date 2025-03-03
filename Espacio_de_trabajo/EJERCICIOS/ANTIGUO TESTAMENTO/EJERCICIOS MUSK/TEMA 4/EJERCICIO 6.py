'''6. Haz un programa que añada un segundo en una hora del día, dadas sus horas, minutos y segundos.'''


h = int(input('Introduce las horas: '))
m = int(input('Introduce los minutos: '))
s = int(input('Introduce los segundos: '))



if s + 1 > 59:
    s = 0
    m += 1
    if m + 1 > 59:
        m = 0
        h += 1
else:
    
    s += 1
    
    
print(f'Horas: {h}, minutos: {m}, segundos: {s}')