def run():

    print("Nivel de rendimiento académico")

    while True:

        entry = input("Ingrese su nota: ").strip()

        # Vacío
        if entry == "":
            print("❌ No puede estar vacío")
            continue

        try:

            grade = int(entry)

            # Rango válido
            if grade < 0 or grade > 100:
                print("❌ La nota debe estar entre 0 y 100")
                continue

            break

        except ValueError:
            print("❌ Debe ingresar números enteros")

    if grade >= 90:
        print("A")

    elif grade >= 80:
        print("B")

    elif grade >= 70:
        print("C")

    else:
        print("D")
