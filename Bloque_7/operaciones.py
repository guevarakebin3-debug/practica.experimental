def run():

    def operations(number):

        double = number * 2
        triple = number * 3
        square = number ** 2

        return double, triple, square


    print("\nEjercicio adicional: calcular doble, triple y cuadrado")

    # Validar número
    while True:

        entry = input("Ingrese un número: ").strip()

        if entry == "":
            print("❌ No puede estar vacío")
            continue

        try:
            num = float(entry)
            break

        except ValueError:
            print("❌ Debe ingresar un número válido")

    d, t, s = operations(num)

    print("Doble:", d)
    print("Triple:", t)
    print("Cuadrado:", s)
