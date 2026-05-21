def run():

    def double(x):
        return x * 2

    def sum_multiple(*numbers):
        return sum(numbers)

    print("Calcular el doble de un número")

    # Validar número
    while True:

        entry = input("Ingrese un número: ").strip()

        if entry == "":
            print("❌ No puede estar vacío")
            continue

        try:
            number = int(entry)
            break

        except ValueError:
            print("❌ Debe ingresar un número entero")

    print("El doble es:", double(number))

    print("\nSuma de varios números")

    # Validar cantidad
    while True:

        entry = input("¿Cuántos números desea ingresar?: ").strip()

        if entry == "":
            print("❌ No puede estar vacío")
            continue

        try:

            quantity = int(entry)

            if quantity <= 0:
                print("❌ Debe ingresar una cantidad mayor a 0")
                continue

            break

        except ValueError:
            print("❌ Debe ingresar números enteros")

    numbers_list = []

    # Validar números de la lista
    for i in range(quantity):

        while True:

            entry = input(f"Ingrese el número {i + 1}: ").strip()

            if entry == "":
                print("❌  No puede estar vacío")
                continue

            try:

                number = float(entry)
                numbers_list.append(number)
                break

            except ValueError:
                print("❌  Debe ingresar un número válido")

    result = sum_multiple(*numbers_list)

    print("La suma total es:", result)
