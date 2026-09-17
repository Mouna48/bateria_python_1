correctas = int(input("Respuestas correctas: "))
incorrectas = int(input("Respuestas incorrectas: "))
blanco = int(input("Respuestas en blanco: "))

nota_final = (correctas * 5) + (incorrectas * -1) + (blanco * 0)
print(f"Nota final: {nota_final}")