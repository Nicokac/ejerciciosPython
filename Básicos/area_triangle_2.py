while True:
    try:
        base = float(input("Ingrese la base: "))
        altura = float(input("Ingrese la altura: "))

        if base <= 0 or altura <= 0:
            print("Error: La base y la altura deben ser números positivos.")
            continue

        area = (base * altura) / 2
        print(f'El área del triangulo con base {base:.2f} y altura {altura:.2f} es: {area:.2f}')
        break
    except ValueError:
        print("Error: Ingrese un número válido. Por favor, intente nuevamente.")