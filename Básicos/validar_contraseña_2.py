import getpass
import re

intentos = 3

while intentos > 0:
    pass_1 = getpass.getpass("Ingrese una contraseña: ")

    if len(pass_1) < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
        intentos -= 1
        print(f'Te quedan {intentos} intentos.')
        continue
    if not re.search("[a-z]", pass_1):
        print("La contraseña debe contener al menos una letra minúscula.")
        intentos -= 1
        print(f'Te quedan {intentos} intentos.')
        continue
    if not re.search("[A-Z]", pass_1):
        print("La contraseña debe contener al menos una letra mayúscula.")
        intentos -= 1
        print(f'Te quedan {intentos} intentos.')
        continue
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", pass_1):
        print("La contraseña debe contener al menos un carácter especial.")
        intentos -= 1
        print(f'Te quedan {intentos} intentos.')
        continue

    pass_2 = getpass.getpass("Ingrese nuevamente la contraseña para confirmarla: ")

    if pass_1 == pass_2:
        print("Contraseña creada correctamente.")
        break
    else:
        print("Las contraseñas no coinciden.")
        intentos -= 1
        print(f'Te quedan {intentos} intentos.')

if intentos == 0:
    print("Has agostado todos los intentos. Por favor, intente más tarde.")