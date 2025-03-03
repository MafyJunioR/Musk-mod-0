'''5. Haz un programa que lea un número y que lo escriba del revés.'''


n = int(input('Introduce un numero: '))

n_r = ''


while n > 0:
    n_r += str(n % 10)
    n = n // 10
    print(n_r)
    
