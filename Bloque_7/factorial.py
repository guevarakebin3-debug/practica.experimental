def run():

    def factorial(n):

        if n == 0:
            return 1

        return n * factorial(n - 1)

    print("Calcular factorial recursivo")

    # Dato fijo
    number = 10

    print("El factorial es:", factorial(number))
