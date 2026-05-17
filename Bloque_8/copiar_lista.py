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
    print("Eliminacion, numero max y min de una lista")

    numeros = []

    for i in range(3):

        # Validar número
        while True:

            entrada = input(f"Ingrese el número {i + 1}: ").strip()

            if entrada == "":
                print("❌ No puede estar vacío")
                continue

            try:
                numero = int(entrada)
                numeros.append(numero)
                break

            except ValueError:
                print("❌ Debe ingresar un número entero")

    print("\nLista original:", numeros)

    eliminado = numeros.pop()

    print("Último elemento eliminado:", eliminado)

    print("Número mayor:", max(numeros))
    print("Número menor:", min(numeros))
