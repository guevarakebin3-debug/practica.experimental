def operaciones(numero):

    doble = numero * 2
    triple = numero * 3
    cuadrado = numero ** 2

    return doble, triple, cuadrado


def ejecutar():

    print("Ejercicio adicional")
    print("Calcular doble, triple y cuadrado")

    num = float(input("Ingrese un número: "))

    d, t, c = operaciones(num)

    print("Doble:", d)
    print("Triple:", t)
    print("Cuadrado:", c)
