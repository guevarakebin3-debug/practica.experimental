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

    # VALIDACIÓN DEL NOMBRE
    while True:
        nombre = input("Ingrese nombre del estudiante: ")

        if nombre.strip() == "":
            print("Error: el nombre no puede estar vacío.")
        elif nombre.isdigit():
            print("Error: el nombre no puede ser solo números.")
        else:
            break

    # VALIDACIÓN DE NOTAS
    notas = []

    for i in range(3):
        while True:
            try:
                nota = float(input(f"Ingrese nota {i + 1} (0-10): "))

                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Error: la nota debe estar entre 0 y 10.")
            except ValueError:
                print("Error: debe ingresar un número válido.")

    est = Estudiante(nombre)
    est.mostrar_promedio(notas)
