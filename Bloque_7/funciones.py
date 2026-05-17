def ejecutar():

    def doble(x):
        return x * 2

    def sumar_varios(*numeros):
        return sum(numeros)

    print("Bloque 7")
    print("Ejercicio 1")
    print("Calcular el doble de un número")

    # Validar número
    while True:

        entrada = input("Ingrese un número: ").strip()

        if entrada == "":
            print("❌ No puede estar vacío")
            continue

        try:
            numero = int(entrada)
            break

        except ValueError:
            print("❌ Debe ingresar un número entero")

    print("El doble es:", doble(numero))

    print("\nEjercicio 2")
    print("Suma de varios números")

    # Validar cantidad
    while True:

        entrada = input("¿Cuántos números desea ingresar?: ").strip()

        if entrada == "":
            print("❌ No puede estar vacío")
            continue

        try:

            cantidad = int(entrada)

            if cantidad <= 0:
                print("❌ Debe ingresar una cantidad mayor a 0")
                continue

            break

        except ValueError:
            print("❌ Debe ingresar números enteros")

    lista_numeros = []

    # Validar números de la lista
    for i in range(cantidad):

        while True:

            entrada = input(f"Ingrese el número {i + 1}: ").strip()

            if entrada == "":
                print("❌ No puede estar vacío")
                continue

            try:

                numero = float(entrada)
                lista_numeros.append(numero)
                break

            except ValueError:
                print("❌ Debe ingresar un número válido")

    resultado = sumar_varios(*lista_numeros)

    print("La suma total es:", resultado)
