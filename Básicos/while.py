# Haz un programa que pida al usuario números hasta que ingrese el número 0.
try:
    num_ingresado = int(input("Ingrese un número, esto parara cuando usted ingrese un 0: "))

    while num_ingresado != 0:
        num_ingresado = int(input("Ingrese otro número, esto parará cuando usted ingrese un 0: "))
        
    print(f'Perfecto! hemos detenido la petición de número porque ha ingresado el {num_ingresado}')
except ValueError:
    print("Error: Ingrese un número válido.")