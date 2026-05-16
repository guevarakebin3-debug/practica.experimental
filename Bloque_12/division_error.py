def ejecutar():

    print("Ejercicio 3")
    print("División con manejo de errores")

    try:
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))

        resultado = a / b
        print("Resultado:", resultado)

    except ValueError:
        print("Error: debes ingresar solo números")

    except ZeroDivisionError:
        print("Error: no se puede dividir entre cero")
