def run():

    print("Ejercicio adicional: actualizar lista con manejo de IndexError")

    numbers_list = [10, 20, 30]

    print("Lista:", numbers_list)

    while True:

        try:
            position = int(input("Ingrese la posición (0-2): "))
            new_value = int(input("Ingrese el nuevo valor: "))

            numbers_list[position] = new_value

            print("Lista actualizada:", numbers_list)
            break  # sale si todo está bien

        except ValueError:
            print("❌ Error: debes ingresar solo números")

        except IndexError:
            print("❌ Error: esa posición no existe en la lista")
