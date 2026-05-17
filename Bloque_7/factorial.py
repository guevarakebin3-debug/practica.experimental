def ejecutar():

    def factorial(n):

        if n == 0:
            return 1

        return n * factorial(n - 1)

    print("Bloque 7")
    print("Ejercicio 3")
    print("Calcular factorial recursivo")

    # Validar número
    while True:

        entrada = input("Ingrese un número: ").strip()

        if entrada == "":
            print("❌ No puede estar vacío")
            continue

        try:

            numero = int(entrada)

            if numero < 0:
                print("❌ No se permite números negativos")
                continue

            break

        except ValueError:
            print("❌ Debe ingresar un número entero")

    print("El factorial es:", factorial(numero))
