def ejecutar():

    def operaciones(numero):

        doble = numero * 2
        triple = numero * 3
        cuadrado = numero ** 2

        return doble, triple, cuadrado

    print("Ejercicio adicional")
    print("Calcular doble, triple y cuadrado")

    # Validar número
    while True:

        entrada = input("Ingrese un número: ").strip()

        if entrada == "":
            print("❌ No puede estar vacío")
            continue

        try:
            num = float(entrada)
            break

        except ValueError:
            print("❌ Debe ingresar un número válido")

    d, t, c = operaciones(num)

    print("Doble:", d)
    print("Triple:", t)
    print("Cuadrado:", c)
