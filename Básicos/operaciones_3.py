while True:
    operacion = input("Qué operación quiere realizar: +, -, *, / (o 'q' para salir): ")

    if operacion.lower() == 'q':
        print("Programa terminado.")
        break

    if operacion not in ["+", "-", "*", "/"]:
        print("La selección no es correcta. Intente de nuevo.")
        continue

    try:
        num_1 = float(input(f'Ingrese un número para realizar la {operacion} : '))
        num_2 = float(input(f'Ingresa otro número: '))
    except ValueError:
        print("Error: Ingrese un número válido")
        continue

    if operacion == "+":
        resultado = num_1 + num_2
    elif operacion == "-":
        resultado = num_1 - num_2 
    elif operacion == "*":
        resultado = num_1 * num_2 
    elif operacion == "/":
        if num_2 != 0:
            resultado = num_1 / num_2
        else:
            print("Error: División por cero no permitida")
            continue 
    print(f'{num_1} {operacion} {num_2} = {resultado}')