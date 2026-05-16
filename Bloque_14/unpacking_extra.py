def ejecutar():

    print("Bloque 14 - Unpacking avanzado")

    print("Ejercicio adicional")

    numeros = []

    for i in range(4):
        num = int(input(f"Ingrese número {i + 1}: "))
        numeros.append(num)

    primero, *medio, ultimo = numeros

    suma_medio = sum(medio)

    print("\nLista completa:", numeros)
    print("Primero:", primero)
    print("Medio:", medio)
    print("Ultimo:", ultimo)
    print("Suma del medio:", suma_medio)
