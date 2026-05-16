def ejecutar():

    print("Ejercicio 1")
    print("Lista con 3 elementos y ordenamiento")

    lista = []

    for i in range(3):
        numero = int(input(f"Ingrese el número {i + 1}: "))
        lista.append(numero)

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
