# c °C to f °F: f = c × 1.8 + 32.

FACTOR_CONVERSION = 9/5 # Equivale a 1.8
OFFSET_CONVERSION = 32

try:
    grados_c = float(input("Ingrese los grados Celsius a convertir a Fahrenheit: "))
    f = grados_c * FACTOR_CONVERSION + OFFSET_CONVERSION
    print(f'Los grados {grados_c} ingresados corresponden a {f:.2f} °F')
except ValueError:
    print("Error: Ingrese un número válido. Asegúrese de usar un formato numérico correcto.")
