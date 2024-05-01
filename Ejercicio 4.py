premio = []

for i in range(6):
    ganador = int(input("Escribe el numero ganador:\n"))
    premio.append(ganador)

premio.sort()

print("Los numeros ganadores son:\n" + str(premio))