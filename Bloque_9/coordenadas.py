def ejecutar():

    print("Bloque 9")
    print("Ejercicio 3")
    print("Lista de coordenadas")

    coordenadas = []

    # Validar cantidad de coordenadas
    while True:

        try:
            cantidad = int(input("¿Cuántas coordenadas desea ingresar?: "))

            if cantidad <= 0:
                print("❌ Debe ser mayor a 0")
                continue

            break

        except ValueError:
            print("❌ Debe ingresar un número entero")

    for i in range(cantidad):

        # Validar X
        while True:
            try:
                x = float(input(f"Ingrese x de la coordenada {i + 1}: "))
                break
            except ValueError:
                print("❌ Debe ingresar un número válido")

        # Validar Y
        while True:
            try:
                y = float(input(f"Ingrese y de la coordenada {i + 1}: "))
                break
            except ValueError:
                print("❌ Debe ingresar un número válido")

        coordenadas.append((x, y))

    print("\nCoordenadas ingresadas:")

    for x, y in coordenadas:
        print(f"x = {x}, y = {y}")
