def run():

    print("Crea una tupla e intenta modificarla")

    element1 = input("Ingrese el primer valor: ")
    element2 = input("Ingrese el segundo valor: ")

    tuple_data = (element1, element2)

    print("\nTupla original:", tuple_data)

    new_value = input("Ingrese el nuevo valor para modificar la posición 0: ")

    try:
        tuple_data[0] = new_value
    except TypeError:
        print("❌\nError: las tuplas no se pueden modificar")

    print("\nEjercicio 2")
    print("Uso del unpacking (a, b, resto)")
    print("(100, 200, 300, 400)")

    a, b, *rest = (100, 200, 300, 400)

    print("a =", a)
    print("b =", b)
    print("resto =", rest)

    print("\nEjercicio adicional: muestra el primer y último elemento de una tupla")

    value1 = input("Ingrese el primer valor: ")
    value2 = input("Ingrese el segundo valor: ")
    value3 = input("Ingrese el tercer valor: ")

    tuple2 = (value1, value2, value3)

    print("\nTupla:", tuple2)

    print("Primer elemento:", tuple2[0])
    print("Último elemento:", tuple2[-1])
