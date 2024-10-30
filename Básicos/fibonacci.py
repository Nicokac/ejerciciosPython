# Muestra los primeros 10 números de la serie Fibonacci.
num_ingresado = int(input("Ingrese el número del cual quiere ver los 10 primeros números de fibonacci: "))

A = 0
B = 1

while B < num_ingresado:
    A, B= B, A + B

print(A)
print(B)

for i in range(1, 9):
    k = A + B
    A = B
    B = k
    print(k)
