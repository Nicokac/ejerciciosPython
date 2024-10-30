# Escribe un programa que pida 5 nombres y los guarde en una lista.

nombres = []

for i in range(5):
    nombre = input("Ingrese un nombre para almacenar en la lista: ")
    nombres.append(nombre)

print('Los nombres ingresados son:', nombres)