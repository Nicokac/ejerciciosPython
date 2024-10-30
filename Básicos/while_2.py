# Haz un programa que pida al usuario números hasta que ingrese el número 0.

print("Ingrese números para continuar. Ingrese 0 para detener el programa.")

while True:
    try:
        num_ingresado = int(input("Ingrese un número: "))

        if num_ingresado == 0:
            print("Perfecto! Hemos detenido la petición de números porque ingresaste el 0.")
            break
            
    except ValueError:
        print("Error: Ingrese un número válido.")