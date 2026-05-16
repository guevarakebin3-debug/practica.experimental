def ejecutar():

    print("Bloque 15 - filter + lambda")

    print("Ejercicio 2 - Obtener números mayores a 3")

    numeros = []

    for i in range(3):
        num = int(input(f"Ingrese número {i + 1}: "))
        numeros.append(num)

    resultado = list(filter(lambda x: x > 3, numeros))

    print("\nLista original:", numeros)
    print("Mayores a 3:", resultado)
