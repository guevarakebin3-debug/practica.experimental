def run():

    print("ValueError al ingresar un número")

    while True:

        try:
            number = int(input("Ingrese un número: "))
            print("Número ingresado:", number)
            break  # sale si es válido

        except ValueError:
            print("❌ Error: Debes ingresar un número válido")
