def run():

    print("División con manejo de errores")

    while True:

        try:
            num1 = int(input("Ingrese el primer número: "))
            num2 = int(input("Ingrese el segundo número: "))

            result = num1 / num2
            print("Resultado:", result)
            break  # sale si todo está bien

        except ValueError:
            print("❌ Error: debes ingresar solo números")

        except ZeroDivisionError:
            print("❌ Error: no se puede dividir entre cero")
