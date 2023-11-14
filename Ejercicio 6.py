# Definir la lista de asignaturas
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# Crear una lista para almacenar las asignaturas a repetir
asignaturas_a_repetir = []

# Preguntar al usuario por la nota de cada asignatura y eliminar las aprobadas
for asignatura in asignaturas:
    nota = float(input(f"Ingresa la nota de {asignatura}: "))
    if nota < 5.0:
        asignaturas_a_repetir.append(asignatura)

# Mostrar las asignaturas a repetir
if asignaturas_a_repetir:
    print("Debes repetir las siguientes asignaturas:")
    for asignatura in asignaturas_a_repetir:
        print(asignatura)
else:
    print("¡Felicidades! Has aprobado todas las asignaturas.")
