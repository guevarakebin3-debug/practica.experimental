class ValidationMixin:
    def validate_email(self, email):
        return "@" in email and email.endswith(".com")

    def validate_age(self, age):
        return age >= 18


class User(ValidationMixin):
    def register(self, name, age, email):

        if not self.validate_age(age):
            print("Edad inválida (debe ser mayor o igual a 18)")
            print("Intenta registrarte nuevamente\n")
            return

        if not self.validate_email(email):
            print("❌ Correo inválido")
            print("❌ Intenta registrarte nuevamente\n")
            return

        print("\nUsuario registrado correctamente")
        print("Nombre:", name)
        print("Edad:", age)
        print("Correo:", email)


def run():

    user = User()

    while True:

        print("\n--- Registro ---")

        name = input("Nombre: ")

        try:
            age = int(input("Edad: "))
        except ValueError:
            print("❌ Edad inválida")
            print("❌ Debes registrarte nuevamente\n")
            continue

        if not user.validate_age(age):
            print("❌ Edad inválida")
            print("❌ Debes registrarte nuevamente\n")
            continue

        email = input("Correo: ")

        if not user.validate_email(email):
            print("❌ Correo inválido")
            print("❌ Debes registrarte nuevamente\n")
            continue

        user.register(name, age, email)

        print("Proceso finalizado correctamente")
        break
