def ejecutar():

    print("Bloque 11")

    print("Ejercicio 2")
    print("Eliminar duplicados con set")

    # Validar cantidad
    while True:
        try:
            cantidad = int(input("¿Cuántos números vas a ingresar?: "))

            if cantidad < 0:
                print("❌ No puede ser negativo")
            else:
                break

        except ValueError:
            print("❌ Debe ingresar un número entero")

    lista = []

    for i in range(cantidad):

        # Validar cada número
        while True:
            try:
                num = int(input(f"Ingrese el número {i + 1}: "))
                lista.append(num)
                break
            except ValueError:
                print("❌ Debe ingresar un número entero")

    print("\nLista original:", lista)

    sin_duplicados = list(set(lista))

    print("Sin duplicados:", sin_duplicados)
