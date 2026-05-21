import json

def run():

    print("Ejercicio - JSON")

    data = {"x": 10, "y": 20}

    # GUARDAR
    with open("data.json", "w") as file:
        json.dump(data, file)

    # CARGAR
    with open("data.json", "r") as file:
        loaded = json.load(file)

    print("Datos cargados:", loaded)
    print("Valor de x:", loaded["x"])


    print("\nEjercicio 3 - Lista JSON interactiva")

    users = []

    for i in range(2):
        print(f"\nUsuario {i + 1}")
        name = input("Ingrese nombre: ")
        age = int(input("Ingrese edad: "))

        users.append({
            "nombre": name,
            "edad": age
        })

    # GUARDAR EN JSON
    with open("users.json", "w") as file:
        json.dump(users, file, indent=2)

    # LEER JSON
    with open("users.json", "r") as file:
        data = json.load(file)

    print("\n--- USUARIOS GUARDADOS ---")
    for user in data:
        print("Nombre:", user["nombre"], "- Edad:", user["edad"])

