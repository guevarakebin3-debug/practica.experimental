def ejecutar():


    print("Ejercicio 2")
    print("IndexError interactivo")

    lista = []

    for i in range(3):
        num = int(input(f"Ingrese el número {i + 1}: "))
        lista.append(num)

    print("\nTu lista es:", lista)

    try:
        pos = int(input("\n¿Qué posición quieres ver? (0-2): "))
        print("Valor en esa posición:", lista[pos])

    except IndexError:
        print("Error: esa posición no existe en la lista")
