def ejecutar():
    print("Ejercicio 1")
    print("Crear un diccionario")

    # Validar nombre (NO números)
    while True:

        nombre = input("Ingrese su nombre: ").strip()

        if nombre.replace(" ", "").isalpha():
            break
        else:
            print("❌ El nombre no puede contener números")

    # Validar edad
    while True:

        try:
            edad = int(input("Ingrese su edad: "))

            if edad < 0:
                print("❌ No puede ser negativa")
            else:
                break

        except ValueError:
            print("❌ Debe ingresar un número entero")

    ciudad = input("Ingrese su ciudad: ").strip()

    persona = {
        "nombre": nombre,
        "edad": edad,
        "ciudad": ciudad,
    }

    print("\n--- Acceso con [] ---")
    print("Nombre:", persona["nombre"])
    print("Edad:", persona["edad"])
    print("Ciudad:", persona["ciudad"])

    print("\n--- Acceso con get() ---")
    print("Nombre:", persona.get("nombre"))
    print("Edad:", persona.get("edad"))
    print("Ciudad:", persona.get("ciudad"))
    print("Teléfono:", persona.get("telefono", "No existe"))

    print("\nEjercicio 2")
    print("Mostrar claves y valores")

    # Validar segunda persona
    while True:

        nombre = input("Ingrese su nombre: ").strip()

        if nombre.replace(" ", "").isalpha():
            break
        else:
            print("❌ El nombre no puede contener números")

    while True:

        try:
            edad = int(input("Ingrese su edad: "))

            if edad < 0:
                print("❌ No puede ser negativa")
            else:
                break

        except ValueError:
            print("❌ Debe ingresar un número entero")

    ciudad = input("Ingrese su ciudad: ").strip()

    persona = {
        "nombre": nombre,
        "edad": edad,
        "ciudad": ciudad
    }

    print("\n--- Claves y valores ---")

    for clave, valor in persona.items():
        print(clave, ":", valor)
