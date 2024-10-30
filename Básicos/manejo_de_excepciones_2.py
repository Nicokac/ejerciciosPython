# MANEJO DE EXCEPCIONES.
# Implementa un programa que pida al usuario un número 
# y maneje errores de entrada incorrecta.

while True:

    try:
        entrada = input("Ingrese un número (o escriba 'salir' para termiar): ")

        if entrada.lower() == 'salir':
            print("Programa terminado por el usuario.")
            break

        numero = int(entrada)
        if numero < 0:
            print("Error: Ingrese un número positivo.")
            continue

        print(f'El número ingresado es {numero}')
        break

    except ValueError:
        print("Error: Ingrese un número válido.")
