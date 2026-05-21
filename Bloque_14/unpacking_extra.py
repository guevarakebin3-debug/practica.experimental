def run():

    print("Ejercicio adicional: Unpacking de una lista")

    numbers_list = []

    for i in range(4):
        while True:
            try:
                num = int(input(f"Ingrese número {i + 1}: "))
                numbers_list.append(num)
                break
            except ValueError:
                print("❌ Error: debe ingresar un número entero válido.")

    first, *middle, last = numbers_list

    middle_sum = sum(middle)

    print("\nLista completa:", numbers_list)
    print("Primero:", first)
    print("Medio:", middle)
    print("Último:", last)
    print("Suma del medio:", middle_sum)
