def ejecutar():

    print("Ejercicio adicional")
    print("Actualizar lista con manejo de IndexError")

    lista = [10, 20, 30]

    print("Lista:", lista)

    while True:

        try:
            pos = int(input("Ingrese la posición (0-2): "))
            nuevo_valor = int(input("Ingrese el nuevo valor: "))

            lista[pos] = nuevo_valor

            print("Lista actualizada:", lista)
            break  # sale si todo está bien

        except ValueError:
            print("❌ Error: debes ingresar solo números")

        except IndexError:
            print("❌ Error: esa posición no existe en la lista")
