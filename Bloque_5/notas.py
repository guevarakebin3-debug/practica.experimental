def ejecutar():
    print("Nivel de rendimiento académico")

    while True:

        entrada = input("Ingrese su nota: ").strip()

        # Vacío
        if entrada == "":
            print("❌ No puede estar vacío")
            continue

        try:

            nota = int(entrada)

            # Rango válido
            if nota < 0 or nota > 100:
                print("❌ La nota debe estar entre 0 y 100")
                continue

            break

        except ValueError:
            print("❌ Debe ingresar números enteros")

    if nota >= 90:
        print("A")

    elif nota >= 80:
        print("B")

    elif nota >= 70:
        print("C")

    else:
        print("D")
