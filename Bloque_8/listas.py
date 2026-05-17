def ejecutar():

    print("Ejercicio 1")
    print("Lista ordenada con 3 elementos ")

    lista = []

    for i in range(3):

        # Validar número
        while True:

            entrada = input(f"Ingrese el número {i + 1}: ").strip()

            if entrada == "":
                print("❌ No puede estar vacío")
                continue

            try:
                numero = int(entrada)
                lista.append(numero)
                break

            except ValueError:
                print("❌ Debe ingresar un número entero")

    print("Lista original:", lista)

    lista.sort()

    print("Lista ordenada:", lista)

    print("\nEjercicio 2")
    print("Suma, máximo y mínimo")

    nums = [5, 3, 8, 1, 9, 3]

    print("Lista:", nums)

    print("Suma:", sum(nums))
    print("Máximo:", max(nums))
    print("Mínimo:", min(nums))
