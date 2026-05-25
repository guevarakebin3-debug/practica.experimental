def run():

    print("Solicitud de nombre y edad")

    # Datos fijos
    name = "Angel"
    age = 20

    # Validar nombre
    if name == "":
        print("❌ El nombre no puede estar vacío")

    elif not name.isalpha():
        print("❌ El nombre solo debe contener letras")

    # Validar edad
    elif age < 0:
        print("❌ La edad no puede ser negativa")

    elif age > 120:
        print("❌ Edad no válida")

    else:
        print(f"Hola {name}, tienes {age} años.")



