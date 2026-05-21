def run():

    print("Obtener números mayores a 3 usando filter")

    numbers = [1, 2, 3, 4, 5]

    result = list(filter(lambda x: x > 3, numbers))

    print("Lista original:", numbers)
    print("Mayores a 3:", result)
