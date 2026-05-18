def ejecutar():

    print("Obtener números mayores a 3 usando filter")

    numeros = [1, 2, 3, 4, 5]

    resultado = list(filter(lambda x: x > 3, numeros))

    print("Lista original:", numeros)
    print("Mayores a 3:", resultado)
