# Escribe un programa que copie el contenido de un archivo a otro.

with open("hola_mundo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

# Crear y escribir el contenido en un nuevo archivo.

with open("copia_hola_mundo.txt", "w") as archivo_2:
    archivo_2.write(contenido)

print("El contenido ha sido copiado a 'copia_hola_mundo.txt'")

with open("hola_mundo.txt", "r") as archivo:
    contenido_original = archivo.read()
    print("Contenido de 'hola_mundo.txt':")
    print(contenido_original)

with open("copia_hola_mundo.txt", "r") as archivo_2:
    contenido_copiado = archivo_2.read()
    print("El contenido copiado de 'copiado_hola_mundo.txt':")
    print(contenido_copiado)