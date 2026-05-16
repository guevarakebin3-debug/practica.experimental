def ejecutar():

    print("Ejercicio 1")
    print("ValueError")

    try:
        numero = int(input("Ingrese un número: "))
        print("Número ingresado:", numero)

    except ValueError:
        print("Error: Debes ingresar un número válido")
