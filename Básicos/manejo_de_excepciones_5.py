# # MANEJO DE EXCEPCIONES.
# Crea un programa que intente convertir una cadena a un número entero 
# y maneje errores de conversión.

while True:
    try:
        entrada = input("Ingrese una cadena de texto (o coloque 'salir' si quiere terminar.): ").lower()

        if entrada == 'salir':
            print("El programa ha terminado.")
            break
        else:
            convertir = int(entrada)
            print(f'Número convertido con éxito: {convertir}')

    except ValueError:
        print("Error: La cadena ingresada no es un número válido.")