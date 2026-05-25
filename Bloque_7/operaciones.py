def run():

    def operations(number):

        double = number * 2
        triple = number * 3
        square = number ** 2

        return double, triple, square


    print("\nEjercicio adicional: calcular doble, triple y cuadrado")

    # Dato fijo
    num = 5

    d, t, s = operations(num)

    print("Doble:", d)
    print("Triple:", t)
    print("Cuadrado:", s)
