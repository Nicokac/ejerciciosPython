import getpass

while True:
    pass_1 = getpass.getpass("Ingrese una contraseña: ")
    pass_2 = getpass.getpass("Ingrese nuevamente la contraseña: ")

    if pass_1 == pass_2:
        print("Contraseña creada correctamente.")
        break
    else: 
        print("Las contraseñas no coinciden.")

