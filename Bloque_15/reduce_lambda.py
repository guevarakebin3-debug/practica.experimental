from functools import reduce

def run():

    print("Multiplica todos los elementos con reduce")

    numbers = [1, 2, 3, 4]

    result = reduce(lambda x, y: x * y, numbers)

    print("Lista:", numbers)
    print("Resultado de la multiplicación:", result)


    print("\nEjercicio adicional: Multiplicación con reduce")

    # Datos fijos
    numbers = [5, 2, 3]

    print("\nLista ingresada:", numbers)

    result = reduce(lambda x, y: x * y, numbers)

    print("Resultado:", result)
