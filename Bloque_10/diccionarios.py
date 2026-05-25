def run():

    print("Crear un diccionario")

    # Datos fijos
    person = {
        "nombre": "Carlos",
        "edad": 20,
        "ciudad": "Guayaquil",
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

    # Segunda persona fija
    person = {
        "nombre": "Ana",
        "edad": 25,
        "ciudad": "Quito"
    }

    print("\n--- Claves y valores ---")

    for key, value in person.items():
        print(key, ":", value)


