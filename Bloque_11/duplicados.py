def ejecutar():

    print("Bloque 11")

    print("Ejercicio 2")
    print("Eliminar duplicados con set")

    cantidad = int(input("¿Cuántos números vas a ingresar?: "))

    lista = []

    for i in range(cantidad):
        num = int(input(f"Ingrese el número {i + 1}: "))
        lista.append(num)

    print("\nLista original:", lista)

    sin_duplicados = list(set(lista))

    print("Sin duplicados:", sin_duplicados)
