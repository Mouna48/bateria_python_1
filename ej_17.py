hh = int(input("Hora de salida (HH): "))
mm = int(input("Minutos de salida (MM): "))
ss = int(input("Segundos de salida (SS): "))
t = int(input("Tiempo de viaje en segundos (T): "))

segundos_totales_salida = (hh * 3600 )+ (mm * 60 ) + ss
segundos_totales_llegada = segundos_totales_salida + t

hora_llegada = (segundos_totales_llegada // 3600) % 24
minutos_llegada = (segundos_totales_llegada % 3600) // 60
segundos_llegada = segundos_totales_llegada % 60

print(f"Hora de llegada: {hora_llegada:02d}:{minutos_llegada:02d}:{segundos_llegada:02d}")