def run():

    print("Copia de diccionarios")
    print("a : 1 , b = 2")

    data = {
        "a": 1,
        "b": 2
    }

    copy_data = data  # referencia, no copia real

    copy_data["b"] = 99

    print("Datos original:", data)
    print("Copia:", copy_data)
