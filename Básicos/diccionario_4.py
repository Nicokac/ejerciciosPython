# Realiza un programa que cuente la cantidad de veces que aparece cada palabra en una frase.

frase = """El sol brilla en el cielo y el cielo es azul. El sol es brillante y el cielo es amplio.
        El día es claro y el cielo se ilumina con el sol. El sol y el cielo son hermosos juntos. 
        La luz del sol llena el cielo y el cielo se vuelve resplandeciente."""

palabras = ["sol", "cielo"]

for palabra in palabras:
    print(f'La palabra "{palabra}" aparece {frase.count(palabra)} veces.')