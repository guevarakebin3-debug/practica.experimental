def ejecutar():

    print("Bloque 15")

    print("Ejercicio 1 - Incrementar en 1")

    numeros = []

    for i in range(3):
        num = int(input(f"Ingrese número {i + 1}: "))
        numeros.append(num)

    resultado = list(map(lambda x: x + 1, numeros))

    print("Lista original:", numeros)
    print("Resultado:", resultado)


    print("\nEjercicio 2 - Filtrar mayores a 3")

    numeros = []

    for i in range(3):
        num = int(input(f"Ingrese número {i + 1}: "))
        numeros.append(num)

    resultado = list(filter(lambda x: x > 3, numeros))

    print("\nLista original:", numeros)
    print("Mayores a 3:", resultado)


    print("\nEjercicio 3 - Multiplicación con reduce")

    from functools import reduce

    numeros = []

    for i in range(3):
        num = int(input(f"Ingrese número {i + 1}: "))
        numeros.append(num)

    resultado = reduce(lambda x, y: x * y, numeros)

    print("\nLista:", numeros)
    print("Resultado:", resultado)


    print("\nEjercicio adicional")

    from functools import reduce

    numeros = []

    for i in range(3):
        num = int(input(f"Ingrese número {i + 1}: "))
        numeros.append(num)

    print("\nLista ingresada:", numeros)

    resultado = reduce(lambda x, y: x * y, numeros)

    print("Resultado final:", resultado)
