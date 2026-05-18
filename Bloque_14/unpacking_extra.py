def ejecutar():

    print("Ejercicio adicional_ Unpacking de una lista")

    numeros = []

    for i in range(4):
        while True:
            try:
                num = int(input(f"Ingrese número {i + 1}: "))
                numeros.append(num)
                break
            except ValueError:
                print("Error: debe ingresar un número entero válido.")

    primero, *medio, ultimo = numeros

    suma_medio = sum(medio)

    print("\nLista completa:", numeros)
    print("Primero:", primero)
    print("Medio:", medio)
    print("Ultimo:", ultimo)
    print("Suma del medio:", suma_medio)
