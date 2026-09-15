minutos_totales = int(input("Introduce la cantidad total de minutos: "))
horas = minutos_totales // 60
minutos_restantes = minutos_totales % 60
print(f"{minutos_totales} minutos corresponden a: {horas} horas y {minutos_restantes} minutos.")
