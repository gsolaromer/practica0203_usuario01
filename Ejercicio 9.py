# Pedimos al usuario que ingrese una palabra
palabra_usuario = input("Ingresa una palabra: ")

# Convertimos la palabra a minúsculas para hacer la cuenta sin distinción entre mayúsculas y minúsculas
palabra_usuario = palabra_usuario.lower()

# Inicializamos una tupla con las vocales
vocales = ('a', 'e', 'i', 'o', 'u')

# Inicializamos una lista para almacenar los contadores de cada vocal
conteo_vocales = [0] * len(vocales)

# Iteramos sobre cada caracter de la palabra
for caracter in palabra_usuario:
    # Verificamos si el caracter es una vocal
    if caracter in vocales:
        # Incrementamos el contador correspondiente en la lista
        indice_vocal = vocales.index(caracter)
        conteo_vocales[indice_vocal] += 1

# Mostramos el resultado
for vocal, conteo in zip(vocales, conteo_vocales):
    print(f"La vocal {vocal} aparece {conteo} veces en la palabra.")