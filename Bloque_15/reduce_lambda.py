from functools import reduce

def run():

    print("Multiplica todos los elementos con reduce")

    numbers = [1, 2, 3, 4]

    result = reduce(lambda x, y: x * y, numbers)

    print("Lista:", numbers)
    print("Resultado de la multiplicación:", result)


    print("\nEjercicio adicional: Multiplicación con reduce")

    numbers = []

    for i in range(3):
        while True:
            try:
                num = int(input(f"Ingrese número {i + 1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("❌ Error: debe ingresar un número entero válido.")

    print("\nLista ingresada:", numbers)

    result = reduce(lambda x, y: x * y, numbers)

    print("Resultado:", result)
