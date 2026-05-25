# MIXIN DE VALIDACIONES
class ValidacionMixin:

    def validar_edad(self, edad):

        if edad < 0:
            print("❌ Edad inválida")
            return False

        return True

    # Solo validación de cédula agregada
    def validar_cedula(self, cedula):

        if len(cedula) != 10 or not cedula.isdigit():
            print("❌ Cédula inválida")
            return False

        return True


# MIXIN DE PROMEDIO
class PromedioMixin:

    def calcular_promedio(self, notas):
        return sum(notas) / len(notas)


# CLASE PRINCIPAL
class SistemaEstudiantes(ValidacionMixin, PromedioMixin):

    def __init__(self):
        self.estudiantes = []
        

    def registrar(self, nombre, edad, cedula, notas):

    

        if not self.validar_edad(edad):
            return

        if not self.validar_cedula(cedula):
            return

        promedio = self.calcular_promedio(notas)

        self.estudiantes.append({
            "Nombre": nombre,
            "edad": edad,
            "cedula": cedula,
            "promedio": promedio
        })

        print("✅ Estudiante registrado")

    def mostrar(self):

        print("\n=== ESTUDIANTES ===")

        for estudiante in self.estudiantes:
            print(estudiante)


# ===== MRO =====

class A:

    def metodo(self):
        print("A")


class B:

    def metodo(self):
        print("B")


class C(A, B):
    pass


# ===== EJECUCIÓN =====

def run():

    sistema = SistemaEstudiantes()

    sistema.registrar(
        "Daniel",
        20,
        "1234567890",
        [8, 9, 10]
    )

    sistema.mostrar()

    print("\n=== MRO ===")
    C().metodo()

