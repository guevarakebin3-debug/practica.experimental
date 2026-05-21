def run():

    def factorial(n):

        if n == 0:
            return 1

        return n * factorial(n - 1)

    print("Calcular factorial recursivo")

    # Validar número
    while True:

        entry = input("Ingrese un número: ").strip()

        if entry == "":
            print("No puede estar vacío")
            continue

        try:

            number = int(entry)

            if number < 0:
                print("No se permite números negativos")
                continue

            break

        except ValueError:
            print("❌ Debe ingresar un número entero")

    print("El factorial es:", factorial(number))
