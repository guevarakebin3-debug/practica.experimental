class PromedioMixin:
    def calcular_promedio(self, notas):
        return sum(notas) / len(notas)


class Estudiante(PromedioMixin):
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_promedio(self, notas):
        promedio = self.calcular_promedio(notas)
        print(f"\nEstudiante: {self.nombre}")
        print("Promedio:", promedio)


def ejecutar():

    print("Bloque 17 - PromedioMixin")

    nombre = input("Ingrese nombre del estudiante: ")

    notas = []

    for i in range(3):
        nota = float(input(f"Ingrese nota {i + 1}: "))
        notas.append(nota)

    est = Estudiante(nombre)
    est.mostrar_promedio(notas)
