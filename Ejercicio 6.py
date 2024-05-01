materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
calificaciones=[]
for i in materias:
    cal = float(input("Cuando sacaste en "+ i + ":\n"))
    calificaciones.append(cal)

for j in range(5):
    if calificaciones[j]<5:
        print("Tienes que repetir la materia de "+ materias[j])