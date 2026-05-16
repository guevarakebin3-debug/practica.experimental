def ejecutar():

    print("Bloque 14")

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


    print("\nEjercicio 3 - Unpacking de diccionarios")

    dict1 = {
        "nombre": input("Ingrese su nombre: "),
        "edad": int(input("Ingrese su edad: "))
    }

    dict2 = {
        "ciudad": input("Ingrese su ciudad: "),
        "pais": input("Ingrese su país: ")
    }

    combinado = {**dict1, **dict2}

    print("\nDiccionario 1:", dict1)
    print("Diccionario 2:", dict2)
    print("Combinado:", combinado)


    print("\nEjercicio adicional - Unpacking avanzado")

    numeros = []

    for i in range(4):
        num = int(input(f"Ingrese número {i + 1}: "))
        numeros.append(num)

    primero, *medio, ultimo = numeros

    suma_medio = sum(medio)

    print("\nLista completa:", numeros)
    print("Primero:", primero)
    print("Medio:", medio)
    print("Ultimo:", ultimo)
    print("Suma del medio:", suma_medio)
