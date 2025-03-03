import string
    
def crear_26():
    
    for letra in string.ascii_uppercase:
        with open(f'{letra}.txt','w' ,encoding='utf-8') as f:
            f.write('')
            
            
crear_26()