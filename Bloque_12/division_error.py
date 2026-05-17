def ejecutar():

    print("Ejercicio 3")
    print("División con manejo de errores")

    while True:

        try:
            a = int(input("Ingrese el primer número: "))
            b = int(input("Ingrese el segundo número: "))

            resultado = a / b
            print("Resultado:", resultado)
            break  # sale si todo está bien

        except ValueError:
            print("❌ Error: debes ingresar solo números")

        except ZeroDivisionError:
            print("❌ Error: no se puede dividir entre cero")
