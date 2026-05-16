class Estudiante:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        if notas is None:
            self.notas = []
        else:
            self.notas = notas

    @classmethod
    def desde_diccionario(cls, datos):
        return cls(datos["nombre"], datos.get("notas"))


def ejecutar():

    print("=== EJERCICIO 1 ===")
    print("Ingresa los datos del estudiante")

    nombre = input("Nombre: ")
    notas = list(map(float, input("Notas: ").split()))

    estudiante = Estudiante(nombre, notas)

    print("Resultado:")
    print(estudiante.nombre, estudiante.notas)

    print("\n=== EJERCICIO 2 (Decorador / classmethod) ===")
    print("Ingresa los datos del estudiante")

    nombre = input("Nombre: ")
    notas = list(map(float, input("Notas: ").split()))

    datos = {
        "nombre": nombre,
        "notas": notas
    }

    estudiante2 = Estudiante.desde_diccionario(datos)

    print("Resultado:")
    print(estudiante2.nombre, estudiante2.notas)
