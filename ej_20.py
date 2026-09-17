m2 = int(input("Monedas de 2€: "))
m1 = int(input("Monedas de 1€: "))
m50 = int(input("Monedas de 50c: "))
m20 = int(input("Monedas de 20c: "))
m10 = int(input("Monedas de 10c: "))

centimos_totales = (m2 * 200) + (m1 * 100) + (m50 * 50) + (m20 * 20) + (m10 * 10)

euros = centimos_totales // 100
centimos = centimos_totales % 100

print(f"Tienes {euros} euros y {centimos} céntimos.")