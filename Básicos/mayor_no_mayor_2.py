# Implementa un programa que pida la edad del usuario y determine si es mayor de edad.
while True:
    try:
        edad = int(input("Ingrese su edad: "))

        if edad < 0:
            print("Error: La edad no puede ser negativa.")
            continue
        if edad >= 18:
            print("Usted es maayor de edad.")
        else:
            print("Usted es menor de edad.")
        break

    except ValueError:
        print("Error: Ingrese un número válido.")