try:
    numero = int(input("Ingrese un número entero para verificar si es par o impar: "))

    if numero % 2 == 0:
            print(f'El número {numero} es par')
    else:
            print(f'El número {numero} es impar')
    print(f'El resto de la división por 2 es {numero % 2}.')
except ValueError:
    print("Error: Ingrese un número válido.")