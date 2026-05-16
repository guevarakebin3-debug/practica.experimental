def ejecutar():

    print("Bloque 16")

    print("Ejercicio 2 - JSON")

    import json

    datos = {"x": 10, "y": 20}

    # GUARDAR
    with open("datos.json", "w") as f:
        json.dump(datos, f)

    # CARGAR
    with open("datos.json", "r") as f:
        cargado = json.load(f)

    print("Datos cargados:", cargado)
    print("Valor de x:", cargado["x"])


    print("\nEjercicio 3 - Lista JSON interactiva")

    usuarios = []

    for i in range(2):
        print(f"\nUsuario {i + 1}")
        nombre = input("Ingrese nombre: ")
        edad = int(input("Ingrese edad: "))

        usuarios.append({
            "nombre": nombre,
            "edad": edad
        })

    # GUARDAR EN JSON
    with open("usuarios.json", "w") as f:
        json.dump(usuarios, f, indent=2)

    # LEER JSON
    with open("usuarios.json", "r") as f:
        data = json.load(f)

    print("\n--- USUARIOS GUARDADOS ---")
    for u in data:
        print("Nombre:", u["nombre"], "- Edad:", u["edad"])
