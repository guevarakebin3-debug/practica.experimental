from functools import reduce

def ejecutar():

    print(" Multiplica todos los elementos con reduce")

    numeros = [1, 2, 3, 4]

    resultado = reduce(lambda x, y: x * y, numeros)

    print("Lista:", numeros)
    print("Resultado de la multiplicación:", resultado)


    print("\nEjercicio adicional_Multiplicación con reduce")

    numeros = []

    for i in range(3):
        while True:
            try:
                num = int(input(f"Ingrese número {i + 1}: "))
                numeros.append(num)
                break
            except ValueError:
                print("Error: debe ingresar un número entero válido.")

    print("\nLista ingresada:", numeros)

    resultado = reduce(lambda x, y: x * y, numeros)

    print("Resultado:", resultado)
