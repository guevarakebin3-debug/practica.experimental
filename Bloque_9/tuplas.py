def ejecutar():

    print("Ejercicio 1")
    print("Crea una tupla e intenta modificarla")

    elemento1 = input("Ingrese el primer valor: ")
    elemento2 = input("Ingrese el segundo valor: ")

    tupla = (elemento1, elemento2)

    print("\nTupla original:", tupla)

    nuevo_valor = input("Ingrese el nuevo valor para modificar la posición 0: ")

    try:
        tupla[0] = nuevo_valor
    except TypeError:
        print("\nError: las tuplas no se pueden modificar")

    print("\nEjercicio 2")
    print("Uso del unpacking (a, b, resto)")

    a, b, *resto = (100, 200, 300, 400)

    print("a =", a)
    print("b =", b)
    print("resto =", resto)

    print("\nEjercicio adicional")
    print("Primer y último elemento de una tupla")

    valor1 = input("Ingrese el primer valor: ")
    valor2 = input("Ingrese el segundo valor: ")
    valor3 = input("Ingrese el tercer valor: ")

    tupla2 = (valor1, valor2, valor3)

    print("\nTupla:", tupla2)

    print("Primer elemento:", tupla2[0])
    print("Último elemento:", tupla2[-1])
