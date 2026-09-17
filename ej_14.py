num = int(input("Introduce un número de dos cifras: "))
decenas = num // 10
unidades = num % 10
num_invertido = unidades * 10 + decenas

print(f"Número invertido: {num_invertido}")