# Pedir al usuario una muestra de números separados por comas
entrada_usuario = input("Ingrese una muestra de números separados por comas: ")

# Convertir la entrada del usuario en una lista de números
numeros = [float(numero) for numero in entrada_usuario.split(',')]

# Calcular la media
media = sum(numeros) / len(numeros)

# Calcular la suma de los cuadrados de las diferencias respecto a la media
suma_cuadrados_diferencias = sum((numero - media) ** 2 for numero in numeros)

# Calcular la desviación típica
desviacion_tipica = (suma_cuadrados_diferencias / len(numeros)) ** 0.5

# Mostrar los resultados por pantalla
print(f"La media de la muestra es: {media}")
print(f"La desviación típica de la muestra es: {desviacion_tipica}")