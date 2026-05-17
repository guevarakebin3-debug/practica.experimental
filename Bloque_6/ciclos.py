def ejecutar():
    print("\nEjercicio 1")
    print("Imprime números del 1 al 10")

    contador = 1

    while contador <= 10:
        print(contador)
        contador += 1


    
    print("\nEjercicio 2")
    print("Enumerate con frutas")

    frutas = ["manzana", "pera", "uva"]

    for indice, fruta in enumerate(frutas):
        print(indice, fruta)



    

    print("\nEjercicio 3")
    print("Cuadrados pares entre 1 y 10")

    cuadrados = [x**2 for x in range(1, 11) if x % 2 == 0]

    print(cuadrados)
