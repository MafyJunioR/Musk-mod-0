with open('data1.txt', 'r') as archivo:
    lineas   = archivo.readlines()
    
for l in lineas:
    print(l.replace('\n',' '))