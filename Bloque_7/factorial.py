def doble(x):
    return x * 2


def sumar_varios(*numeros):
    return sum(numeros)


def ejecutar():

    print("Bloque 7")
    print("Ejercicio 1")
    print("Calcular el doble de un número")

    numero = int(input("Ingrese un número: "))

    print("El doble es:", doble(numero))

    print("\nEjercicio 2")
    print("Suma de varios números")

    cantidad = int(input("¿Cuántos números desea ingresar?: "))

    lista_numeros = []

    for i in range(cantidad):
        numero = float(input(f"Ingrese el número {i + 1}: "))
        lista_numeros.append(numero)

    resultado = sumar_varios(*lista_numeros)

    print("La suma total es:", resultado)
