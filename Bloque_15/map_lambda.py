def ejecutar():

    print("Bloque 15 - map + lambda")

    print("Ejercicio 1 - Incrementa en 1 cada elemento de la lista")

    numeros = []

    for i in range(3):
        num = int(input(f"Ingrese número {i + 1}: "))
        numeros.append(num)

    resultado = list(map(lambda x: x + 1, numeros))

    print("Lista original:", numeros)
    print("Resultado:", resultado)
