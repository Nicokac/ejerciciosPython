# MANEJO DE EXCEPCIONES.
# Realiza un programa que abra un archivo que no exista 
# y maneje el error adecuadamente.

try:
    with open("archivo_prueba.txt", "r") as fichero:
        leer_fichero = fichero.read()
        print(leer_fichero)
        
except FileNotFoundError:
    print("El archivo 'archivo_prueba.txt' no existe o no pudo abrirse.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")