def run():

    print("Archivos py")

    while True:
        text = input("Escribe 'Python': ")

        if text == "Python":
            break
        else:
            print("❌ Error: debes escribir exactamente 'Python'.")

    # ESCRIBIR
    with open("archivo.txt", "w") as file:
        file.write(text + "\n")

    # LEER
    with open("archivo.txt", "r") as file:
        print("\nContenido del archivo:")
        print(file.read())
