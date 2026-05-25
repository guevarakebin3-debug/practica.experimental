def run():

    print("Diferencia simétrica")

    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}

    result = (set_a | set_b) - (set_a & set_b)

    print("Conjunto A:", set_a)
    print("Conjunto B:", set_b)
    print("Resultado:", result)

    print("\nEjercicio adicional: Operaciones completas entre conjuntos")

    # Datos fijos
    set_a = {10, 20, 30}
    set_b = {20, 40, 50}

    print("\nConjunto A:", set_a)
    print("Conjunto B:", set_b)

    print("\nUnión:", set_a | set_b)
    print("Intersección:", set_a & set_b)
    print("Diferencia (A - B):", set_a - set_b)
    print("Diferencia simétrica:", set_a ^ set_b)


