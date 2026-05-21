def run():

    print("Lista ordenada con 3 elementos")

    numbers_list = []

    for i in range(3):

        # Validar número
        while True:

            entry = input(f"Ingrese el número {i + 1}: ").strip()

            if entry == "":
                print("❌ No puede estar vacío")
                continue

            try:
                number = int(entry)
                numbers_list.append(number)
                break

            except ValueError:
                print("❌ Debe ingresar un número entero")

    print("Lista original:", numbers_list)

    numbers_list.sort()

    print("Lista ordenada:", numbers_list)

    print("\nSuma, máximo y mínimo")

    nums = [5, 3, 8, 1, 9, 3]

    print("Lista:", nums)

    print("Suma:", sum(nums))
    print("Máximo:", max(nums))
    print("Mínimo:", min(nums))
