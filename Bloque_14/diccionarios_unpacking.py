def ejecutar():

    print("Combinación de 2 diccionarios usando **")

    dict1 = {
        "nombre": "Juan",
        "edad": 20
    }

    dict2 = {
        "ciudad": "Milagro",
        "pais": "Ecuador"
    }

    combinado = {**dict1, **dict2}

    print("\nDiccionario 1:", dict1)
    print("Diccionario 2:", dict2)
    print("Combinado:", combinado)
