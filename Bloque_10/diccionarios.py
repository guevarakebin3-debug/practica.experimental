def ejecutar():

    print("Bloque 10")

    print("Ejercicio 1")
    print("Crear un diccionario")

    persona = {
        "nombre": input("Ingrese su nombre: "),
        "edad": int(input("Ingrese su edad: ")),
        "ciudad": input("Ingrese su ciudad: "),
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

    persona = {
        "nombre": input("Ingrese su nombre: "),
        "edad": int(input("Ingrese su edad: ")),
        "ciudad": input("Ingrese su ciudad: ")
    }

    print("\n--- Claves y valores ---")

    for clave, valor in persona.items():
        print(clave, ":", valor)
