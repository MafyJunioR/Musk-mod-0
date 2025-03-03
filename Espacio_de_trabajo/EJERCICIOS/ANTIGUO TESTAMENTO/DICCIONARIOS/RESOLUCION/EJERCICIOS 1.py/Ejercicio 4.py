'''
Crea un diccionario llamado `personas` que contenga información sobre dos personas,
cada una con detalles como nombre, edad y lista de hobbies.


1. Accede al nombre de "Persona1" e imprímelo.
2. Imprime todos los hobbies de "Persona2".
3. Agrega un nuevo hobby a la lista de hobbies de "Persona1".
4. Imprime la estructura completa del diccionario.
'''

personas = {
    'Persona1': {
        'nombre':'George',
        'edad':'26',
        'hobbies':['jugar', 'correr']
    },
    'Persona2': {
        'nombre': 'Oihane',
        'edad': '24',
        'hobbies':['escribir','tocar la guitarra']
    }
}

Persona1 = personas['Persona1']
Persona2 = personas['Persona2']

nombre_Persona1 = personas['Persona1']['nombre']
print(f'El nombre de Persona1 es: {nombre_Persona1}')
print(Persona2['hobbies'])
hobbies_Persona1 = personas['Persona1']['hobbies']
hobbies_Persona1.append('Sudoku')
print(personas)