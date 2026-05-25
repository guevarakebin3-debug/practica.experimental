def run():
    print("Promedio de dos números")

    # Datos fijos
    num1 = 10
    num2 = 20

    # Validación
    if not isinstance(num1, (int, float)):
        print("❌ El primer valor no es un número válido")

    elif not isinstance(num2, (int, float)):
        print("❌ El segundo valor no es un número válido")

    else:
        suma = num1 + num2
        promedio = suma / 2

        print("Suma:", suma)
        print("Promedio:", promedio)
