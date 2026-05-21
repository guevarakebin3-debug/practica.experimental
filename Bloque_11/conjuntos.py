def run():

    print("Conjuntos interactivos")

    set_a = set()
    set_b = set()

    # Validar cantidad A
    while True:
        try:
            size_a = int(input("¿Cuántos números tendrá el conjunto A?: "))
            if size_a < 0:
                print("No puede ser negativo")
            else:
                break
        except ValueError:
            print("Debe ingresar un número entero")

    # Llenar A
    for i in range(size_a):

        while True:
            try:
                num = int(input(f"Ingrese número {i + 1} para A: "))
                set_a.add(num)
                break
            except ValueError:
                print("Debe ingresar un número entero")

    # Validar cantidad B
    while True:
        try:
            size_b = int(input("\n¿Cuántos números tendrá el conjunto B?: "))
            if size_b < 0:
                print("No puede ser negativo")
            else:
                break
        except ValueError:
            print("Debe ingresar un número entero")

    # Llenar B
    for i in range(size_b):

        while True:
            try:
                num = int(input(f"Ingrese número {i + 1} para B: "))
                set_b.add(num)
                break
            except ValueError:
                print("Debe ingresar un número entero")

    print("\nConjunto A:", set_a)
    print("Conjunto B:", set_b)

    print("\nUnión (A | B):", set_a | set_b)
    print("Intersección (A & B):", set_a & set_b)
    print("Diferencia (A - B):", set_a - set_b)
