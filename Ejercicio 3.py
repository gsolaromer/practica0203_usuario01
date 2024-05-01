materias= ["Matematicas", "Física", "Química", "Historia", "Lengua", "Biología"]

calificaciones = []

for i in materias:
    cal=float(input("Cuanto sacaste en " + i + ":\n"))
    calificaciones.append(cal)

for j in range(len(materias)):
    print("En " + materias[j] + " has sacado: " + str(calificaciones[j]))