def ejecutar():

    print("Bloque 16")

    print("Ejercicio 1 - Archivos")

    # ESCRIBIR
    with open("archivo.txt", "w") as f:
        f.write("Python\n")

    # LEER
    with open("archivo.txt", "r") as f:
        contenido = f.read()
        print("Contenido del archivo:")
        print(contenido)
