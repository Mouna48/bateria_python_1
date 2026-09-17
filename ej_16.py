distancia = float(input("Distancia entre vehículos (km): "))
v1 = float(input("Velocidad del más rápido (km/h): "))
v2 = float(input("Velocidad del más lento (km/h): "))

tiempo_horas = distancia / (v1 - v2)
tiempo_minutos = tiempo_horas * 60

print(f"El vehículo más rápido alcanzará al otro en {tiempo_minutos:.2f} minutos.")