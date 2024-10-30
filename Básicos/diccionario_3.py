# Añade una nueva clave-valor a un diccionario.

alumno = {
    "nombre": "Nicolás",
    "edad": 32,
    "materia": "base de datos"
          }

nombre = alumno["nombre"]
print(nombre)

# Modificar el valor clave de una existente
alumno["nombre"] = "Matias"
nombre_2 = alumno["nombre"]
print(nombre_2)

# Añade una nueva clave-valor al diccionario
alumno["ciudad"] = "Buenos Aires"
print(alumno)