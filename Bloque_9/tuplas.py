def run():

    print("Crea una tupla e intenta modificarla")

    # Datos fijos
    element1 = "Hola"
    element2 = "Mundo"

    tuple_data = (element1, element2)

    print("\nTupla original:", tuple_data)

    new_value = "Python"

    try:
        tuple_data[0] = new_value
    except TypeError:
        print("❌\nError: las tuplas no se pueden modificar")


    print("\nUso del unpacking (a, b, resto)")
    print("(100, 200, 300, 400)")

    a, b, *rest = (100, 200, 300, 400)

    print("a =", a)
    print("b =", b)
    print("resto =", rest)

    print("\nEjercicio adicional: Muestra el primer y último elemento de una tupla")

    # Datos fijos
    value1 = "Rojo"
    value2 = "Verde"
    value3 = "Azul"

    tuple2 = (value1, value2, value3)

    print("\nTupla:", tuple2)

    print("Primer elemento:", tuple2[0])
    print("Último elemento:", tuple2[-1])

