# Escribe un programa que permita gestionar un inventario de productos.

productos = {
    "nombre": ["Fideos", "Arroz", "Azucar"],
    "marca": ["Favorita", "Moneda", "Ledesma"],
    "peso kg.": [1, 0.500, 1],
    "color": ["Amarillo", "Blanco", "Blanco"],
}

# ver los productos
print("Inventario iniciales:")
for i in range(len(productos["nombre"])):
    print(f'Producto {i+1}:')
    print(f' Nombre: {productos["nombre"][i]}')
    print(f' Marca: {productos["marca"][i]}')
    print(f' Peso: {productos["peso kg."][i]}')
    print(f' Color: {productos["color"][i]}\n')

# agregar un nuevo producto
nuevo_nombre = "Pan"
nueva_marca = "Bimbo"
nuevo_peso = 0.500
nuevo_color = "Blanco"
productos["nombre"].append(nuevo_nombre)
productos["marca"].append(nueva_marca)
productos["peso kg."].append(nuevo_peso)
productos["color"].append(nuevo_color)
print(f'Producto {nuevo_nombre} añadido con éxito.\n')

# Eliminar un producto existente
producto_a_eliminar = "Arroz"
if producto_a_eliminar in productos["nombre"]:
    idx = productos["nombre"].index(producto_a_eliminar)
    for key in productos.keys():
        productos[key].pop(idx)
    print(f'Producto {producto_a_eliminar} eliminado con éxito.\n')
else:
    print(f'Producto {producto_a_eliminar} no encontrado.\n')

# Actualizar un producto existente
producto_a_actualizar = "Azucar"
nuevo_nombre = "Azucar Morena"
nueva_marca = "Cañuela"
nuevo_peso = 1.2
nuevo_color = "Marrón"

if producto_a_actualizar in productos["nombre"]:
    idx = productos["nombre"].index(producto_a_actualizar)
    productos["nombre"][idx] = nuevo_nombre
    productos["marca"][idx] = nueva_marca
    productos["peso kg."][idx] = nuevo_peso
    productos["color"][idx] = nuevo_color
    print(f'Producto {producto_a_actualizar} actualizado con éxito.\n')
else:
    print(f'Producto {producto_a_actualizar} no encontrado.\n')

# Ver los productos actualizados
print("Inventario actualizado:")
for i in range(len(productos["nombre"])):
    print(f'Producto {i+1}:')
    print(f' Nombre: {productos["nombre"][i]}')
    print(f' Marca: {productos["marca"][i]}')
    print(f' Peso: {productos["peso kg."][i]}')
    print(f' Color: {productos["color"][i]}\n')
