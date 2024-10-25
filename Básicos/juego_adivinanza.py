# Crea un juego que adivine un número del 1 al 10.

NUMERO = 10
intentos = 3

while intentos > 0:
    try:
        num_ingresado = int(input("Ingrese un número del 1 al 10: "))
        if num_ingresado == NUMERO:
            print(f'Correcto! El número ingresado {num_ingresado} es igual a {NUMERO}')
            break
        else:
            print(f'El número {num_ingresado} no es correcto.')
            intentos -= 1
            print(f'Le quedan {intentos} intentos.')
    except ValueError:
        print("Error: Ingrese un número válido.")
if intentos == 0:
    print(f'Se acabaron los intentos. El número correcto era {NUMERO}')
    