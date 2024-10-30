# Escribe un programa que cree un archivo de texto y escriba "Hola, Mundo!" en él.

# Abrir (o crear, en caso de que no exista) un archivo llamado "hola_mundo.txt" en modo de escritura ("w")
with open("hola_mundo.txt", "w") as archivo:
    archivo.write("Hola, Mundo!")

print("El archivo ha sido creado y el mensaje ha sido escrito.")