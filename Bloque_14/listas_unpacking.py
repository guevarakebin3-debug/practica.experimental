def ejecutar():

    print("Bloque 14 - Unpacking en listas")

    print("Ejercicio 1 - Unpacking")

    numeros = []

    for i in range(4):
        num = int(input(f"Ingrese número {i + 1}: "))
        numeros.append(num)

    primera, *mitad, ultima = numeros

    print("\nLista completa:", numeros)
    print("Primera:", primera)
    print("Mitad:", mitad)
    print("Ultima:", ultima)


    print("\nEjercicio 2 - Multiplicar con unpacking")

    def multiplicar(a, b, c):
        return a * b * c

    lista = []

    for i in range(3):
        num = int(input(f"Ingrese número {i + 1}: "))
        lista.append(num)

    resultado = multiplicar(*lista)

    print("Lista:", lista)
    print("Resultado:", resultado)
