# Crea una función que convierta una lista de temperaturas en Celsius a Fahrenheit.

def celcius_fahrenheit(grados_c):
    FACTOR_CONVERSION = 9/5
    OFFSET_CONVERSION = 32
    grados_f = grados_c * FACTOR_CONVERSION + OFFSET_CONVERSION
    return grados_f

try: 
    c = 30
    f = celcius_fahrenheit(float(c))
    print(f'{c}°C => {f}°F')
except ValueError as e:
    print(f'Error: {e}')