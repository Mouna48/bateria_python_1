nombre = input("Nombre: ")
apellido1 = input("Primer apellido: ")
apellido2 = input("Segundo apellido: ")

iniciales = f"{nombre[0]}{apellido1[0]}{apellido2[0]}".upper()
print(f"Iniciales: {iniciales}")