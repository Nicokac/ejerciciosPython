# Realiza un programa que permita al usuario escribir múltiples líneas y las guarde en un archivo.

with open("archivo_5.txt", "w") as archivo:
    archivo.write("Hola, Mundo!")

with open("archivo_5.txt", "r") as archivo:
    contenido_original = archivo.read()
    print(f'El contenido es: {contenido_original}')

lista = ["Estoy agregando líneas\n", "Esta es otra línea\n", "La última línea\n"]

with open("archivo_5.txt", "a") as archivo:
    archivo.writelines(lista)

with open("archivo_5.txt", "r") as archivo:
    contenido_agregado = archivo.read()
    print(f'El contenido es: {contenido_agregado}')
