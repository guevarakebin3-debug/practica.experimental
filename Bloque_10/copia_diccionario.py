def ejecutar():

    print("Ejercicio 3")
    print("Copia de diccionarios")
    print("a : 1 , b = 2")

    datos = {
        "a": 1,
        "b": 2
    }

    copia = datos  # referencia, no copia real

    copia["b"] = 99

    print("Datos original:", datos)
    print("Copia:", copia)
