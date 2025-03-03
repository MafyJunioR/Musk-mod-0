'''La temperatura en °C se puede convertir a °F usando esta fórmula:
°F = (°C x 9/5) + 32.
Escribe una función que convierta °C a °F,
convert_celsius_to-fahrenheit .'''


def convert_celsius_to_fahrenheit(a):
    F = (a * 9/5) + 32
    
    return (f'{a} grados Celsius son {F} grados Fahrenheit')


print(convert_celsius_to_fahrenheit(9))