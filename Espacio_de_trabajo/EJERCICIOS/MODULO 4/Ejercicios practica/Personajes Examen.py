personajes_principales = [
    ("Astarion", 239, "Rogue", "Elf", 3, True),
    ("Shadowheart", 40, "Cleric", "Half-Elf", 5, True),
    ("Wyll", 25, "Warlock", "Human", 2, False),
    ("Gale", 35, "Wizard", "Human", 5, True),
    ("Karlach", 32, "Barbarian", "Tiefling", 6, False),
    ("Lae'zel", 20, "Fighter", "Githyanki", 4, True),
    ("Jaheira", 150, "Druid", "Half-Elf", 6, False),
    ("Halsin", 350, "Druid", "Elf", 7, False),
    ("Minsc", 130, "Ranger", "Human", 5, False),
    ("Minthara", 250, "Paladin", "Drow", 8, False),
    ("Dark Urge", 30, "Sorcerer", "Dragonborn", 1, False)
]

# Ejercicio 1: Calcular el nivel medio del equipo
def calcular_nivel_medio(personajes):
    suma = 0
    contador = 0
    for personaje in personajes:
        if personaje[5]:
            suma += personaje[4]
            contador += 1
    media = suma // contador
    return media

print(calcular_nivel_medio(personajes_principales))
print('------------------------------------')

# Ejercicio 2: Filtrar personajes en el equipo

def filtrar(personajes):
    equipo = []
    for personaje in personajes:
        if personaje[5]:
            equipo.append(personaje)
    return equipo

print(filtrar(personajes_principales))
print('------------------------------------')

# Ejercicio 3: Conjunto de clases únicas

def obtener_clases(personajes):
    clases = set()
    for personaje in personajes:
        clases.add(personaje[2])
        
    return clases

print(obtener_clases(personajes_principales))
print('------------------------------------')

# Ejercicio 4: Conteo de Personajes por Raza

def contar_raza(personajes):
    conteo_razas = {}
    for personaje in personajes:
        raza = personaje[3]
        if raza in conteo_razas:
            conteo_razas[raza] += 1
        else:
            conteo_razas[raza] = 1
            
    return conteo_razas
print(contar_raza(personajes_principales))
print('------------------------------------')

# Ejercicio 5: Verificación de Existencia de Raza

def verificar_raza(personajes, raza):
    for personaje in personajes:
        if raza == personaje[3]:
            return True
    return False

print(verificar_raza(personajes_principales, 'Human'))
print(verificar_raza(personajes_principales, 'Gnome'))
print('------------------------------------')

# Ejercicio 6: Personaje con Mayor Nivel

def personaje_mayor_nivel(personajes, clase=None):
    nombre = None
    maximo = 0
    for personaje in personajes:
        if clase == None or personaje[2] == clase:
            if personaje[4] > maximo:
                nombre = personaje[0]
                maximo = personaje[4]
            
    return nombre

print(personaje_mayor_nivel(personajes_principales))
print(personaje_mayor_nivel(personajes_principales, 'Cleric'))
print('------------------------------------')

# Ejercicio 7: Incrementar Nivel de un Personaje

def incrementar_nivel(personajes, nombre):
    for i in range(len(personajes)):
        if personajes[i][0] == nombre:
            personajes[i] = (personajes[i][0],
                             personajes[i][1],
                             personajes[i][2],
                             personajes[i][3],
                             personajes[i][4]+1,
                             personajes[i][5])
            
incrementar_nivel(personajes_principales, 'Halsin')
print(personajes_principales[7])
print('------------------------------------')

# Ejercicio 8: Programa un juego - Adivina la edad del personaje

def adivinar_edad(personajes):
    nombre = input('Introduzca el nombre: ').lower
    
    for personaje in personajes:
        if personaje[0] == nombre:
            real = personaje[1]
            break
    
    jugando = True
    
    while(jugando):
        edad = int(input('Introduzca su edad: '))
        if edad == 0:
            print('Interrupción por el jugador.')
            break
        
        if edad < real:
            print(f'{nombre} es mayor.')
        elif edad > real:
            print(f'{nombre} es menor.')
        else:
            print('Correcto.')
            jugando = False
            
adivinar_edad(personajes_principales)