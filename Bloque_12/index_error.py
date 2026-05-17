def ejecutar():

    print("IndexError al acceder a numero de la lista")

    lista = []

    # Validar números de la lista
    for i in range(3):

        while True:
            try:
                num = int(input(f"Ingrese el número {i + 1}: "))
                lista.append(num)
                break
            except ValueError:
                print("❌ Debe ingresar un número entero")

    print("\nTu lista es:", lista)

    # Validar posición
    while True:

        try:
            pos = int(input("\n¿Qué posición quieres ver? (0-2): "))

            print("Valor en esa posición:", lista[pos])
            break

        except ValueError:
            print("❌ Debe ingresar un número entero")

        except IndexError:
            print("❌ Esa posición no existe en la lista")
