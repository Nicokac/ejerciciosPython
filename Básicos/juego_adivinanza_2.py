# Crea un juego que adivine un número del 1 al 10.

import random

RANGO_MIN = 1
RANGO_MAX = 10
INTENTOS_MAX = 3

NUMERO = random.randint(RANGO_MIN, RANGO_MAX)
intentos = INTENTOS_MAX

print(f'¡Bienvenidos al juego de adivinar el número! Tienes que adivinar un número del 1 al 10. Contas con {INTENTOS_MAX} intentos.')

while intentos > 0:
    try: 
        num_ingresado = int(input("Ingrese un número del 1 al 10: "))
        if not RANGO_MIN <= num_ingresado <= RANGO_MAX:
            print(f'Error: El número debe estar dentro del rango de {RANGO_MIN} y {RANGO_MAX}')
            continue

        if num_ingresado == NUMERO:
            print(f'Correcto! El número ingresado {num_ingresado} es igual a {NUMERO}. Has ganado!')
            break
        else:
            print(f'El número {num_ingresado} no es correcto.')
            intentos -= 1
            print(f'Te quedan {intentos} intentos.')

            if intentos > 0:
                if num_ingresado < NUMERO:
                    print("Pista: El número es más alto.")
                else:
                    print("Pista: El número es más bajo.")
    except ValueError:
        print("Error: Ingrese un número válido.")

if intentos == 0:
    print(f'Se acabaron los intentos. El número correcto era {NUMERO}. Gracias por jugar!')