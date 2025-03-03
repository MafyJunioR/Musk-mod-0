'''5. Haz un programa que añada una nueva cadena en medio de una cadena dada.'''


texto1= input('Introduce un texto: ')
texto2= input('Introduce texto para meter en medio del texto anterior: ')



en_medio = len(texto1) // 2

annadido = texto1[:en_medio:]

annadido += texto2

annadido += texto1[en_medio:]

print(annadido)