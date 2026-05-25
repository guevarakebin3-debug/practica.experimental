def run():

    print("Eliminar duplicados con set")

    # Datos fijos
    numbers_list = [1, 2, 2, 3, 4, 4, 5]

    print("\nLista original:", numbers_list)

    no_duplicates = list(set(numbers_list))

    print("Sin duplicados:", no_duplicates)

