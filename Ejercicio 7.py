# Crear una lista con el abecedario
abecedario = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

# Eliminar las letras que ocupan posiciones múltiplos de 3
abecedario_filtrado = [letra for i, letra in enumerate(abecedario) if (i + 1) % 3 != 0]

# Mostrar la lista resultante
print(abecedario_filtrado)
