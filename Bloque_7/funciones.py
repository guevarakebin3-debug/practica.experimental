def run():

    def double(x):
        return x * 2

    def sum_multiple(*numbers):
        return sum(numbers)

    print("Calcular el doble de un número")

    # Dato fijo
    number = 8

    print("El doble es:", double(number))

    print("\nSuma de varios números")

    # Datos fijos
    numbers_list = [10, 20, 30, 40]

    result = sum_multiple(*numbers_list)

    print("La suma total es:", result)

