def run():

    print("Imprime números del 1 al 10")

    counter = 1

    while counter <= 10:
        print(counter)
        counter += 1

    print("\nEnumerate con frutas")

    fruits = ["manzana", "pera", "uva"]

    for index, fruit in enumerate(fruits):
        print(index, fruit)

    print("\nCuadrados pares entre 1 y 10")

    squares = [x**2 for x in range(1, 11) if x % 2 == 0]

    print(squares)
