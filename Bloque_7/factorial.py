def factorial(n):

    if n == 0:
        return 1

    return n * factorial(n - 1)


def ejecutar():

    print("Bloque 7")
    print("Ejercicio 3")
    print("Calcular factorial recursivo")

    numero = int(input("Ingrese un número: "))

    print("El factorial es:", factorial(numero))
