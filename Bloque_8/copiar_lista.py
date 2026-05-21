def run():

    print("Copia de listas y referencias")

    numbers_list = [1, 2, 3]

    copy_list = numbers_list

    copy_list.append(4)

    print("Lista original:", numbers_list)
    print("Copia:", copy_list)

    print("\nEjercicio adicional: eliminación, número máximo y mínimo de una lista")

    numbers = []

    for i in range(3):

        # Validar número
        while True:

            entry = input(f"Ingrese el número {i + 1}: ").strip()

            if entry == "":
                print("❌ No puede estar vacío")
                continue

            try:
                number = int(entry)
                numbers.append(number)
                break

            except ValueError:
                print("❌ Debe ingresar un número entero")

    print("\nLista original:", numbers)

    removed = numbers.pop()

    print("Último elemento eliminado:", removed)

    print("Número mayor:", max(numbers))
    print("Número menor:", min(numbers))
