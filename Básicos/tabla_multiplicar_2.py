# Genera una tabla de multiplicar de un número ingresado por el usuario.

try:
    num_ingresado = int(input("Ingrese un número del cual quiera obtener su tabla de multiplicación: "))

    print(f'\nTabla de multiplicar del {num_ingresado}:')
    for i in range(1, 11):
        resultado = i * num_ingresado
        print(f'{num_ingresado} x {i} = {resultado}')
        
except ValueError:
    print("Error: Ingrese un número válido.")