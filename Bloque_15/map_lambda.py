def ejecutar():

    print("Bloque 15 - map + lambda")
    print("Incrementa en 1 cada elemento de la lista usando map")

    numeros = [2, 4, 6]

    resultado = list(map(lambda x: x + 1, numeros))

    print("Lista original:", numeros)
    print("Resultado:", resultado)
