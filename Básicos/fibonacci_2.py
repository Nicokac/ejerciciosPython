# Muestra 10 números de Fibonacci empezando desde el número ingresado por el usuario.
num_ingresado = int(input("Ingrese un número para comenzar la serie Fibonacci: "))

# Inicializar la serie
A, B = 0, 1

# Encuentra el punto de inicio cercano al número ingresado
while A < num_ingresado:
    A, B = B, A + B

# Muestra el número ingresado y los 10 siguientes en la serie de Fibonacci
print(f'El número inicial encontrado en la serie es {A}')
for _ in range(10):  # Mostrar 10 números después del punto inicial
    A, B = B, A + B
    print(A)