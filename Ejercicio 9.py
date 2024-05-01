palabra = input("Escribe la palabra:\n")
vocales = ["a", "e", "i", "o", "u"]
cont = 0
for vocal in vocales:
    cont = 0
    for letra in palabra:
        if vocal == letra:
            cont+=1
print("La palabra: " + palabra +" tiene: " + str(cont) + " " + vocal)