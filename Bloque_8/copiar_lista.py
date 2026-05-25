def run():

    print("Copia de listas y referencias")

    numbers_list = [1, 2, 3]

    copy_list = numbers_list

    copy_list.append(4)

    print("Lista original:", numbers_list)
    print("Copia:", copy_list)

    print("\nEjercicio adicional: eliminación, número máximo y mínimo de una lista")

    # Datos fijos
    fixed_numbers = [10, 25, 7]

    numbers = []

    for number in fixed_numbers:

        # Validaciones
        if str(number).strip() == "":
            print("❌ No puede estar vacío")
            continue

        try:
            value = int(number)
            numbers.append(value)

        except ValueError:
            print("❌ Debe ingresar un número entero")

    print("\nLista original:", numbers)

    removed = numbers.pop()

    print("Último elemento eliminado:", removed)

    print("Número mayor:", max(numbers))
    print("Número menor:", min(numbers))
