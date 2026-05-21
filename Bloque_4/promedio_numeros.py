def run():
    print("Promedio de dos números")

    # Primer número
    while True:
        try:
            num1 = float(input("Ingrese el primer número: "))
            break
        except ValueError:
            print("❌ Debe ingresar un número válido")

    # Segundo número
    while True:
        try:
            num2 = float(input("Ingrese el segundo número: "))
            break
        except ValueError:
            print("❌ Debe ingresar un número válido")

    suma = num1 + num2
    promedio = suma / 2

    print("Suma:", suma)
    print("Promedio:", promedio)
