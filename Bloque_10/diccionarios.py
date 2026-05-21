def run():

    print("Crear un diccionario")

    # Validar nombre (NO números)
    while True:

        name = input("Ingrese su nombre: ").strip()

        if name.replace(" ", "").isalpha():
            break
        else:
            print("El nombre no puede contener números")

    # Validar edad
    while True:

        try:
            age = int(input("Ingrese su edad: "))

            if age < 0:
                print("No puede ser negativa")
            else:
                break

        except ValueError:
            print("Debe ingresar un número entero")

    city = input("Ingrese su ciudad: ").strip()

    person = {
        "nombre": name,
        "edad": age,
        "ciudad": city,
    }

    print("\n--- Acceso con [] ---")
    print("Nombre:", person["nombre"])
    print("Edad:", person["edad"])
    print("Ciudad:", person["ciudad"])

    print("\n--- Acceso con get() ---")
    print("Nombre:", person.get("nombre"))
    print("Edad:", person.get("edad"))
    print("Ciudad:", person.get("ciudad"))
    print("Teléfono:", person.get("telefono", "No existe"))

    print("\nMostrar claves y valores")

    # Validar segunda persona
    while True:

        name = input("Ingrese su nombre: ").strip()

        if name.replace(" ", "").isalpha():
            break
        else:
            print("El nombre no puede contener números")

    while True:

        try:
            age = int(input("Ingrese su edad: "))

            if age < 0:
                print("No puede ser negativa")
            else:
                break

        except ValueError:
            print("Debe ingresar un número entero")

    city = input("Ingrese su ciudad: ").strip()

    person = {
        "nombre": name,
        "edad": age,
        "ciudad": city
    }

    print("\n--- Claves y valores ---")

    for key, value in person.items():
        print(key, ":", value)
