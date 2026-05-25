# MIXIN 1
class SaludoMixin:

    def saludar(self):
        print(f"Hola, soy {self.nombre}")


# MIXIN 2
class TrabajoMixin:

    def trabajar(self):
        print(f"{self.nombre} está trabajando")


# Clase que hereda de los 2 mixins
class Empleado(SaludoMixin, TrabajoMixin):

    def __init__(self, nombre, cargo):
        self.nombre = nombre
        self.cargo = cargo

    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Cargo:", self.cargo)


# Otra clase que también hereda de los mixins
class Estudiante(SaludoMixin, TrabajoMixin):

    def __init__(self, nombre, carrera):
        self.nombre = nombre
        self.carrera = carrera

    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Carrera:", self.carrera)

def run():
# ===== CREAR OBJETOS =====

    empleado1 = Empleado("Carlos", "Programador")
    empleado2 = Empleado("Ana", "Diseñadora")

    estudiante1 = Estudiante("Luis", "Ingeniería")
    estudiante2 = Estudiante("María", "Medicina")


# ===== MOSTRAR EN CONSOLA =====

    print("\n--- EMPLEADOS ---")

    empleado1.saludar()
    empleado1.trabajar()
    empleado1.mostrar_datos()

    print()
    empleado2.saludar()
    empleado2.trabajar()
    empleado2.mostrar_datos()


    print("\n--- ESTUDIANTES ---")

    estudiante1.saludar()
    estudiante1.trabajar()
    estudiante1.mostrar_datos()

    print()

    estudiante2.saludar()
    estudiante2.trabajar()
    estudiante2.mostrar_datos()






class ValidationMixin:

    def validar_edad(self, edad):

        if edad >= 18:
            return True

        return False


class Usuario(ValidationMixin):

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)


def ejecutar():

    usuario1 = Usuario("Kebin", 18)

    if usuario1.validar_edad(usuario1.edad):

        print("Edad válida")
        usuario1.mostrar()

    else:
        print("Edad inválida")

