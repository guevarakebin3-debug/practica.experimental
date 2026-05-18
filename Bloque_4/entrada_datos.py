def ejecutar():

    print("Solicitud de nombre y edad")

    # Validar nombre
    while True:

        nombre = input("Ingrese su nombre: ").strip()

        if nombre == "":
            print("❌ El nombre no puede estar vacío")

        elif not nombre.isalpha():
            print("❌ El nombre solo debe contener letras")

        else:
            break
    # Validar edad
    while True:

        try:

            edad = int(input("Ingrese su edad: "))

            if edad < 0:
                print("❌ La edad no puede ser negativa")

            elif edad > 120:
                print("❌ Edad no válida")

            else:
                break

        except ValueError:
            print("❌ Debe ingresar números")

    print(f"Hola {nombre}, tienes {edad} años.")
