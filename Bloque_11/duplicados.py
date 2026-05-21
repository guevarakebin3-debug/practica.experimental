def run():

    print("Eliminar duplicados con set")

    # Validar cantidad
    while True:
        try:
            quantity = int(input("¿Cuántos números vas a ingresar?: "))

            if quantity < 0:
                print("❌ No puede ser negativo")
            else:
                break

        except ValueError:
            print("❌ Debe ingresar un número entero")

    numbers_list = []

    for i in range(quantity):

        # Validar cada número
        while True:
            try:
                num = int(input(f"Ingrese el número {i + 1}: "))
                numbers_list.append(num)
                break
            except ValueError:
                print("❌ Debe ingresar un número entero")

    print("\nLista original:", numbers_list)

    no_duplicates = list(set(numbers_list))

    print("Sin duplicados:", no_duplicates)
