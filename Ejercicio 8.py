palabra = input("Escribe una palabra:\n")

palabra_reves = palabra

palabra = list(palabra)
palabra_reves = list(palabra_reves)
palabra_reves.reverse()

if palabra == palabra_reves:
    print("ES UN PALINDROMO")
else:
    print("NO ES UN PALINDROMO")