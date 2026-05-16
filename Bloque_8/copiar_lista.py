def ejecutar():

    print("Bloque 8")
    print("Ejercicio 3")
    print("Copia de listas y referencias")

    lista = [1, 2, 3]

    copia = lista

    copia.append(4)

    print("Lista original:", lista)
    print("Copia:", copia)

    print("\nEjercicio adicional")
    print("Eliminación y análisis")

    numeros = []

    for i in range(3):
        numero = int(input(f"Ingrese el número {i + 1}: "))
        numeros.append(numero)

    print("\nLista original:", numeros)

    eliminado = numeros.pop()

    print("Último elemento eliminado:", eliminado)

    print("Número mayor:", max(numeros))
    print("Número menor:", min(numeros))
