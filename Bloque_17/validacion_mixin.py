class ValidacionMixin:
    def validar_email(self, correo):
        return "@" in correo and ".com" in correo

    def validar_edad(self, edad):
        return edad >= 18


class Usuario(ValidacionMixin):
    def registrar(self, nombre, edad, correo):

        if not self.validar_email(correo):
            print("❌ Correo inválido")
            return

        if not self.validar_edad(edad):
            print("❌ Edad inválida (debe ser mayor o igual a 18)")
            return

        print("\n✅ Usuario registrado correctamente")
        print("Nombre:", nombre)
        print("Edad:", edad)
        print("Correo:", correo)


def ejecutar():

    print("Bloque 17 - ValidacionMixin")

    nombre = input("Ingrese nombre: ")
    edad = int(input("Ingrese edad: "))
    correo = input("Ingrese correo: ")

    usuario = Usuario()
    usuario.registrar(nombre, edad, correo)
