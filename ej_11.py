numero1 =float(input ("introduce el primer numero :"))
numero2 =float(input ("introduce el segundo numero :"))
if numero1 >= numero2:
    distancia = numero1 - numero2
else: 
    distancia = numero2 - numero1
print(f"la distancia entre {numero1} y {numero2} es: {distancia}")