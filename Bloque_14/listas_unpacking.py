def ejecutar():

    print("Unpacking de listas")

    numeros = (10, 20, 30, 40)

    primera, *mitad, ultima = numeros

    print("\nLista completa:", numeros)
    print("Primera:", primera)
    print("Mitad:", mitad)
    print("Ultima:", ultima)




    print("\nUso de * en funciones")

    def multiplicar(a, b, c):
        return a * b * c

    lista = [2, 3, 4]

    resultado = multiplicar(*lista)

    print("Lista:", lista)
    print("Resultado:", resultado)

