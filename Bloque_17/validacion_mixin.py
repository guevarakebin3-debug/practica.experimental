class ValidacionMixin:
    def validar_email(self, correo):
        return "@" in correo and correo.endswith(".com")

    def validar_edad(self, edad):
        return edad >= 18


class Usuario(ValidacionMixin):
    def registrar(self, nombre, edad, correo):

        if not self.validar_edad(edad):
            print("❌ Edad inválida (debe ser mayor o igual a 18)")
            print("🔁 Intenta registrarte nuevamente\n")
            return

        if not self.validar_email(correo):
            print("❌ Correo inválido")
            print("🔁 Intenta registrarte nuevamente\n")
            return

        print("\n✅ Usuario registrado correctamente")
        print("Nombre:", nombre)
        print("Edad:", edad)
        print("Correo:", correo)


def ejecutar():

    usuario = Usuario()

    while True:

        print("\n--- Registro ---")

        nombre = input("Nombre: ")
        edad = int(input("Edad: "))

        if not usuario.validar_edad(edad):
            print(" Edad inválida")
            print("Debes registrarte nuevamente\n")
            continue

        correo = input("Correo: ")

        if not usuario.validar_email(correo):
            print(" Correo inválido")
            print(" Debes registrarte nuevamente\n")
            continue

        usuario.registrar(nombre, edad, correo)

        print("🎉 Proceso finalizado correctamente")
        break
