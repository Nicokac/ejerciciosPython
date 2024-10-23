operacion = input("Qué operación quiere realizar: +, -, *, /; ")

a = float(input(f'Ingrese un número para realizar la {operacion} : '))
b = float(input(f'Ingresa otro número: '))

if operacion == "+":
    suma = a + b
    print(f'El resultado es: {suma}') 
elif operacion == "-":
    resta = a - b
    print(f'El resultado es: {resta}') 
elif operacion == "*":
    multiplicacion = a * b
    print(f'El resultado es: {multiplicacion}') 
elif operacion == "/":
    if b != 0:
        division = a / b
        print(f'El resultado es: {division}')
    else:
        print("Error: División por cero no permitida") 
else:
    print("La selección no es correcta")

