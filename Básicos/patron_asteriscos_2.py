# Genera un patrón de asteriscos en forma de triángulo.

try:

    num_lineas = int(input("Ingrese el número de líneas para el triángulo: "))

    if num_lineas <= 0:
        print("Por favor, ingrese un número positivo.")
    else:
        print("Generando el triángulo de asteriscos:\n")
        for i in range(1, num_lineas + 1):
            print('*' * i)

except ValueError:
    print("Error: Ingrese un número entero válido.")