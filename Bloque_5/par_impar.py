def run():

    print("Verificar si un número es par o impar")

    while True:

        try:
            number = int(input("Ingrese un número: "))
            break

        except ValueError:
            print("❌ Debe ingresar un número ")

    if number % 2 == 0:
        print("Es par")
    else:
        print("Es impar")
