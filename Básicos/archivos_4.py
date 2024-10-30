# Crea un programa que elimine un archivo.
import pathlib 

with open("copia_hola_mundo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

# Metdoo para borrar el archivo usando pathlib
path = pathlib.Path("copia_hola_mundo.txt")
path.unlink()

print("El archivo ha sido eliminado.")


