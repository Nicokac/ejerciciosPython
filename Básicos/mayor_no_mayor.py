# Implementa un programa que pida la edad del usuario y determine si es mayor de edad.
try:
    edad = int(input("Ingrese su edad: "))

    if edad >= 18: 
        print("Usted es mayor")
    else:
        print("Usted es menor de edad.")
except ValueError:
    print("Error: Ingrese un número válido.")