# MANEJO DE EXCEPCIONES.
# Escribe una función que maneje múltiples tipos de excepciones.

def manejar_excepciones():
    try:

        a = int(input("Ingres el primer número: "))
        b = int(input("Ingrese el segundo número: "))
        suma = a + b
        print(f'La suma de {a} y {b} es: {suma}')

        division = a / b
        print(f'La división de {a} y {b} es: {division:.2f}')

        lista = [1,2,3]
        index = int(input("Ingrese el índice del elemento que desea acceder: "))
        elemento = lista[index]
        print(f'El elemento en el índice {index} es: {elemento}')

    except ValueError as ve:
        print(f'Error de valor: {ve}')

    except ZeroDivisionError as zde:
        print(f'Error de división por cero: {zde}')

    except IndexError as ie:
        print("Error: Índice fuera de rango. Intente con un índice entre 0 y 2.")

    except FileNotFoundError as fnfe:
        print(f'Error de archivo no encontrado: {fnfe}')
    
    except Exception as e:
        print(f'Error inesperado: {e}')

# Ejemplo de uso:
manejar_excepciones()
