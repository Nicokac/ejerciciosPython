# Realiza una función que reciba una cadena de texto y cuente las vocales.

def contar_vocales(frase):
    frase = frase.lower()
    vocales = ["a", "e", "i", "o", "u"]
    conteo = {vocal: frase.count(vocal) for vocal in vocales}
    return conteo 


frase = "Hola, cómo estás. Yo bien por suerte, estoy un poco de triste."
resultado = contar_vocales(frase)
print(resultado)