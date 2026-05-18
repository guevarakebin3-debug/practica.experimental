def ejecutar():

    print("Bloque 16")
    print("Ejercicio 1 - Archivos")

    while True:
        texto = input("Escribe 'Python': ")

        if texto == "Python":
            break
        else:
            print("Error: debes escribir exactamente 'Python'.")

    # ESCRIBIR
    with open("archivo.txt", "w") as f:
        f.write(texto + "\n")

    # LEER
    with open("archivo.txt", "r") as f:
        print("\nContenido del archivo:")
        print(f.read())

