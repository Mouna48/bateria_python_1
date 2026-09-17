las_notas = []
for i in range(1,4):
    notas = float(input(f"Introduce la nota {i}: "))
    las_notas.append(notas)
promedio = sum(las_notas) / len(las_notas)
examen_final = float (input("introduce la nota del examen final: "))
trabajo_final = float (input("introduce  la calificación de un trabajo final:"))
nota_final = (promedio * 0.55) + (examen_final * 0.30 )+ (trabajo_final * 0.15)
print(f"La nota final es: {nota_final:.2f}")