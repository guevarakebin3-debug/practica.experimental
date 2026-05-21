def run():

    print("IndexError al acceder a número de la lista")

    numbers_list = []

    # Validar números de la lista
    for i in range(3):

        while True:
            try:
                num = int(input(f"Ingrese el número {i + 1}: "))
                numbers_list.append(num)
                break
            except ValueError:
                print("❌ Debe ingresar un número entero")

    print("\nTu lista es:", numbers_list)

    # Validar posición
    while True:

        try:
            position = int(input("\n¿Qué posición quieres ver? (0-2): "))

            print("Valor en esa posición:", numbers_list[position])
            break

        except ValueError:
            print("❌Debe ingresar un número entero")

        except IndexError:
            print("❌ Esa posición no existe en la lista")
