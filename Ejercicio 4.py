# Pide al usuario que ingrese los números ganadores de la lotería primitiva uno por uno
print("Introduce los números ganadores de la lotería primitiva (introduce '0' para finalizar):")
numeros_ganadores = []

while True:
    numero = int(input("Número ganador (introduce 0 para finalizar): "))
    if numero == 0:
        break
    numeros_ganadores.append(numero)

# Ordena la lista de números ganadores de menor a mayor
numeros_ganadores.sort()

# Muestra los números ganadores ordenados
print("Números ganadores ordenados de menor a mayor:")
for numero in numeros_ganadores:
    print(numero)
