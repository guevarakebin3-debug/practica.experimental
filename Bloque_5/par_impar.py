def ejecutar():

    print("Verificar si un número es par o impar")

    while True:

        try:

            numero = int(input("Ingrese un número: "))
            break

        except ValueError:
            print("❌ Debe ingresar un número ")

    if numero % 2 == 0:
        print("Es par")
    else:
        print("Es impar")
