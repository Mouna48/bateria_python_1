sueldo_base = float(input("Introduce el sueldo base: "))
venta1 = float(input("Introduce el valor de la primera venta: "))
venta2 = float(input("Introduce el valor de la segunda venta: "))
venta3 = float(input("Introduce el valor de la tercera venta: "))

total_ventas = [venta1, venta2, venta3]
total = 0.0
for venta in total_ventas:
    total += venta

comision = total * 0.10
sueldo_total = sueldo_base + comision

print(f"La comisión obtenida por las ventas es: {comision}")
print(f"El sueldo total del empleado es: {sueldo_total}")