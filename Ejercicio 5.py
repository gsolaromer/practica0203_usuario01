# Crear una lista con los números del 1 al 10
numeros = list(range(1, 11))

# Invertir la lista
numeros_invertidos = list(reversed(numeros))

# Mostrar los números invertidos separados por comas
numeros_en_cadena = ', '.join(map(str, numeros_invertidos))
print(numeros_en_cadena)
