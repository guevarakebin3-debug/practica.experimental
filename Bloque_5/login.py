def ejecutar():

    print("Sistema de login")
    print("Usuario: admin | password: 123")

    usuario = input("Ingrese el usuario: ")
    password = input("Ingrese la contraseña: ")

    if usuario == "admin" and password == "123":
        print("Bienvenido")
    else:
        print("Acceso denegado")
