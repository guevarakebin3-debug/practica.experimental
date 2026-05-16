def ejecutar():

    print("Bloque 9")

    print("Ejercicio 3")
    print("Lista de coordenadas")

    coordenadas = []

    cantidad = int(input("¿Cuántas coordenadas desea ingresar?: "))

    for i in range(cantidad):

        x = float(input(f"Ingrese x de la coordenada {i + 1}: "))
        y = float(input(f"Ingrese y de la coordenada {i + 1}: "))

        coordenadas.append((x, y))

    print("\nCoordenadas ingresadas:")

    for x, y in coordenadas:
        print(f"x = {x}, y = {y}")
