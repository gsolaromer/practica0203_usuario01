precios = [50, 75, 46, 22, 80, 65, 1000]
minimo = maximo = precios[0]

for precio in precios:
    if precio < minimo:
        minimo = precio
    elif precio > maximo:
        maximo = precio
print("El maximo es: " + str (maximo))
print("El minimo es: " + str (minimo))