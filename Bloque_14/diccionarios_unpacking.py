def ejecutar():

    print("Bloque 14 - Unpacking de diccionarios")

    print("Ejercicio 3 - Unpacking de diccionarios")

    dict1 = {
        "nombre": input("Ingrese su nombre: "),
        "edad": int(input("Ingrese su edad: "))
    }

    dict2 = {
        "ciudad": input("Ingrese su ciudad: "),
        "pais": input("Ingrese su país: ")
    }

    combinado = {**dict1, **dict2}

    print("\nDiccionario 1:", dict1)
    print("Diccionario 2:", dict2)
    print("Combinado:", combinado)
