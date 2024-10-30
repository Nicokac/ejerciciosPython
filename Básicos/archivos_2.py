# Realiza un programa que lea un archivo de texto y cuente cuántas palabras contiene.

fichero_1 = open("hola_mundo.txt", "r")

try:
    # Usar el fichero
    print(fichero_1.read())
    pass
finally:
    # Esta sección es siempre ejecutada.
    fichero_1.close()

# ----------------------------------------------------------- #
# Otra forma de leer un archivo.
with open("hola_mundo.txt", "r") as fichero_2:
    # Usar el fichero. Se cerrará automaticamente.
    print(f'El archivo tiene el siguiente texto: {fichero_2.read()}')
    for linea in fichero_2:
        print(linea, end="")

# Realiza un programa que lea un archivo de texto y cuente cuántas palabras contiene.

with open ("hola_mundo.txt", "r") as fichero_3:
    contenido = fichero_3.read() # Lee el contenido
    palabras = contenido.split() # Divide
    cantidad_palabras = len(palabras) # Cuenta la cantidad de palabras 

print(f'El archivo contiene {cantidad_palabras} palabras.') 
