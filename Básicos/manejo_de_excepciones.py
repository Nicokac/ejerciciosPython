# MANEJO DE EXCEPCIONES.
# Escribe un programa que maneje una división por cero.

try:
    num_1 = int(input("Ingrese un número para dividir: "))
    num_2 = int(input("Ingrese divisor: "))
   
    if num_1 < 0 or num_2 < 0:
        print("Ambos números tienen que ser positivos.")
    else:
        resultado = num_1 / num_2
        print(f'El resultado de la división de {num_1} y {num_2} es: {resultado:.3f}')

except ZeroDivisionError:
        print(f'Error: No se puede dividir por cero.')
except ValueError:
    print("Error: Ingrese un número válido.")
