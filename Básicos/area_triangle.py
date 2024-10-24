try:
    base = float(input("Ingrese la base: "))
    altura = float(input("Ingrese la altura: "))
    area = (base * altura) / 2
    print(f'El area del triangulo con base {base:.2f} y altura {altura:.2f} es: {area:.2f}')
except ValueError:
    print("Error: Ingrese un número válido. Por favor, intente nuevamente.")

