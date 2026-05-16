def ejecutar():

    print("Bloque 10")

    print("Ejercicio 3")
    print("Copia de diccionarios")

    datos = {
        "a": 1,
        "b": 2
    }

    copia = datos  # referencia, no copia real

    copia["b"] = 99

    print("Datos original:", datos)
    print("Copia:", copia)

    print("\nEjercicio adicional")
    print("Referencia en diccionarios")

    datos = {
        "a": 10,
        "b": 20
    }

    copia = datos

    copia["b"] = 99

    print("\nDatos original:")
    print(datos)

    print("\nCopia:")
    print(copia)
