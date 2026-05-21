def run():

    print("Lista de coordenadas")

    coordinates = []

    # Validar cantidad de coordenadas
    while True:

        try:
            quantity = int(input("¿Cuántas coordenadas desea ingresar?: "))

            if quantity <= 0:
                print("❌ Debe ser mayor a 0")
                continue

            break

        except ValueError:
            print("❌ Debe ingresar un número entero")

    for i in range(quantity):

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

        coordinates.append((x, y))

    print("\nCoordenadas ingresadas:")

    for x, y in coordinates:
        print(f"x = {x}, y = {y}")
