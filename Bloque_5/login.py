def run():

    print("Sistema de login")
    print("Usuario: admin | password: 123")

    while True:

        user = input("Ingrese el usuario: ")
        password = input("Ingrese la contraseña: ")

        if user == "admin" and password == "123":
            print("✅ Bienvenido")
            break

        else:
            print("❌ Acceso denegado")
            print("Intente nuevamente\n")
