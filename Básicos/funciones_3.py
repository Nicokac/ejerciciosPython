# Implementa una función que verifique si un número es primo.

# Enfoque iterativo 
def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            print("No es primo", {n}, "es divisor")
            return False
    print("Es primo")
    return True

# Enfoque recursivo
def es_primo_2(num, n=2):
    if n >= num:
        print("Es primo")
        return True
    elif num % n !=0:
        return es_primo_2(num, n+1)
    else:
        print("No es primo", {n}, "es divisor")
        return False
    
es_primo(23)
es_primo_2(23)