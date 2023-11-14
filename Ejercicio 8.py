# Pedimos al usuario que ingrese una palabra
palabra_usuario = input("Ingresa una palabra: ")

# Convertimos la palabra a minúsculas para hacer la comparación sin distinción entre mayúsculas y minúsculas
palabra_usuario = palabra_usuario.lower()

# Convertimos la palabra en una lista de caracteres
lista_caracteres = list(palabra_usuario)

# Creamos una tupla con la reversa de la lista de caracteres
tupla_reversa = tuple(reversed(lista_caracteres))

# Comparamos la palabra original con la versión invertida
if lista_caracteres == list(tupla_reversa):
    print(f"{palabra_usuario} es un palíndromo.")
else:
    print(f"{palabra_usuario} no es un palíndromo.")