# Definir las matrices A y B como listas anidadas
matriz_A = [[1, 2, 3],
            [4, 5, 6]]

matriz_B = [[-1, 0],
            [0, 1],
            [1, 1]]

# Inicializar una matriz para el resultado, llena de ceros
filas_A = len(matriz_A)
columnas_A = len(matriz_A[0])
filas_B = len(matriz_B)
columnas_B = len(matriz_B[0])

# Verificar si las matrices son compatibles para la multiplicación
if columnas_A != filas_B:
    print("No se pueden multiplicar las matrices. El número de columnas de A debe ser igual al número de filas de B.")
else:
    # Inicializar la matriz resultado con ceros
    resultado = [[0 for _ in range(columnas_B)] for _ in range(filas_A)]

    # Calcular el producto de las matrices
    for i in range(filas_A):
        for j in range(columnas_B):
            for k in range(filas_B):
                resultado[i][j] += matriz_A[i][k] * matriz_B[k][j]

    # Mostrar el resultado
    print("Matriz A:")
    for fila in matriz_A:
        print(fila)

    print("\nMatriz B:")
    for fila in matriz_B:
        print(fila)

    print("\nProducto de A y B:")
    for fila in resultado:
        print(fila)