def ejecutar():

    print("Ejercicio 1")
    print("ValueError")

    while True:

        try:
            numero = int(input("Ingrese un número: "))
            print("Número ingresado:", numero)
            break  # sale si es válido

        except ValueError:
            print("❌ Error: Debes ingresar un número válido")
