def ejecutar():
    print("Concatenación de texto con el número 5")

    while True:

        numero = input("Ingrese un número: ")

        if numero.isdigit():
            break

        else:
            print("❌ Debe ingresar solo números")

    print(numero + "5")
