def run():

    print("Unpacking de listas")

    numbers = (10, 20, 30, 40)

    first, *middle, last = numbers

    print("\nLista completa:", numbers)
    print("Primera:", first)
    print("Mitad:", middle)
    print("Última:", last)


    print("\nUso de * en funciones")

    def multiply(a, b, c):
        return a * b * c

    nums_list = [2, 3, 4]

    result = multiply(*nums_list)

    print("Lista:", nums_list)
    print("Resultado:", result)
