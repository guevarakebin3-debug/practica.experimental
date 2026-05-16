def ejecutar():

    print("Bloque 11")

    print("Ejercicio 3")
    print("Diferencia simétrica")

    A = {1, 2, 3, 4}
    B = {3, 4, 5, 6}

    resultado = (A | B) - (A & B)

    print("Conjunto A:", A)
    print("Conjunto B:", B)
    print("Resultado:", resultado)

    print("\nEjercicio adicional")
    print("Operaciones completas")

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

    print("\nUnión:", A | B)
    print("Intersección:", A & B)
    print("Diferencia (A - B):", A - B)
    print("Diferencia simétrica:", A ^ B)
