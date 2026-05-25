def run():

    print("Archivos py")

    # Dato fijo
    text = "Python"

    # ESCRIBIR
    with open("archivo.txt", "w") as file:
        file.write(text + "\n")

    # LEER
    with open("archivo.txt", "r") as file:
        print("\nContenido del archivo:")
        print(file.read())

