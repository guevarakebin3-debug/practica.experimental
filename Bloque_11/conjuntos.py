def ejecutar():

    print("Bloque 11")

    print("Ejercicio 1")
    print("Conjuntos interactivos")

    A = set()
    B = set()

    cantidad_a = int(input("¿Cuántos números tendrá el conjunto A?: "))

    for i in range(cantidad_a):
        num = int(input(f"Ingrese número {i + 1} para A: "))
        A.add(num)

    cantidad_b = int(input("\n¿Cuántos números tendrá el conjunto B?: "))

    for i in range(cantidad_b):
        num = int(input(f"Ingrese número {i + 1} para B: "))
        B.add(num)

    print("\nConjunto A:", A)
    print("Conjunto B:", B)

    print("\nUnión (A | B):", A | B)
    print("Intersección (A & B):", A & B)
    print("Diferencia (A - B):", A - B)
