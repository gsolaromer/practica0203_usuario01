# Crear una lista de asignaturas
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# Crear una lista para almacenar las notas
notas = []

# Solicitar al usuario la nota de cada asignatura
for asignatura in asignaturas:
    nota = float(input(f"¿Qué nota has sacado en {asignatura}? "))
    notas.append(nota)

# Mostrar las asignaturas y las notas por pantalla
for i in range(len(asignaturas)):
    print(f"En {asignaturas[i]} has sacado {notas[i]}")
    