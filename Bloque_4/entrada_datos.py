def run():

    print("Solicitud de nombre y edad")

    # Validate name
    while True:

        name = input("Ingrese su nombre: ").strip()

        if name == "":
            print("❌ El nombre no puede estar vacío")

        elif not name.isalpha():
            print("❌ El nombre solo debe contener letras")

        else:
            break

    # Validate age
    while True:

        try:
            age = int(input("Enter your age: "))

            if age < 0:
                print("❌ La edad no puede ser negativa")

            elif age > 120:
                print("❌ Edad no válida")

            else:
                break

        except ValueError:
            print("❌ Debe ingresar números")

    print(f"Hola {name}, tienes {age} años.")
