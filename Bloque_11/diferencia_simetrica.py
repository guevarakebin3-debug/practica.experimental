def run():

    print("Diferencia simétrica")

    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}

    result = (set_a | set_b) - (set_a & set_b)

    print("Conjunto A:", set_a)
    print("Conjunto B:", set_b)
    print("Resultado:", result)

    print("\nEjercicio adicional: operaciones completas entre conjuntos")

    set_a = set()
    set_b = set()

    # Validar cantidad A
    while True:
        try:
            size_a = int(input("¿Cuántos números tendrá el conjunto A?: "))

            if size_a < 0:
                print("❌ No puede ser negativo")
            else:
                break

        except ValueError:
            print("❌ Debe ingresar un número entero")

    # Llenar A
    for i in range(size_a):

        while True:
            try:
                num = int(input(f"Ingrese número {i + 1} para A: "))
                set_a.add(num)
                break

            except ValueError:
                print("❌ Debe ingresar un número entero")

    # Validar cantidad B
    while True:
        try:
            size_b = int(input("\n¿Cuántos números tendrá el conjunto B?: "))

            if size_b < 0:
                print("❌ No puede ser negativo")
            else:
                break

        except ValueError:
            print("❌ Debe ingresar un número entero")

    # Llenar B
    for i in range(size_b):

        while True:
            try:
                num = int(input(f"Ingrese número {i + 1} para B: "))
                set_b.add(num)
                break

            except ValueError:
                print("❌ Debe ingresar un número entero")

    print("\nConjunto A:", set_a)
    print("Conjunto B:", set_b)

    print("\nUnión:", set_a | set_b)
    print("Intersección:", set_a & set_b)
    print("Diferencia (A - B):", set_a - set_b)
    print("Diferencia simétrica:", set_a ^ set_b)
