# Genera una tabla de multiplicar de un número ingresado por el usuario.

num_ingresado = float(input("Ingrese un número del cual quiera obtener su tabla de multiplicación: "))

for i in range(1, 11):
    resultado = i * num_ingresado
    print(f'{num_ingresado} x {i} = {resultado}')