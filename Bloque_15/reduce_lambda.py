from functools import reduce

def ejecutar():

    print("Bloque 15 - reduce + lambda")

    print("Ejercicio 3 - Multiplica todos los elementos")

    numeros = []

    for i in range(3):
        num = int(input(f"Ingrese número {i + 1}: "))
        numeros.append(num)

    resultado = reduce(lambda x, y: x * y, numeros)

    print("\nLista:", numeros)
    print("Resultado de la multiplicación:", resultado)


    print("\nEjercicio adicional")

    numeros = []

    for i in range(3):
        num = int(input(f"Ingrese número {i + 1}: "))
        numeros.append(num)

    print("\nLista ingresada:", numeros)

    resultado = reduce(lambda x, y: x * y, numeros)

    print("Resultado:", resultado)
