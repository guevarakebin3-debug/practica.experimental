class AverageMixin:
    def calculate_average(self, grades):
        return sum(grades) / len(grades)


class Student(AverageMixin):
    def __init__(self, name):
        self.name = name

    def show_average(self, grades):
        average = self.calculate_average(grades)
        print(f"\nEstudiante: {self.name}")
        print("Promedio:", average)


def run():

    print("PromedioMixin")

    # VALIDACIÓN DEL NOMBRE
    while True:
        name = input("Ingrese nombre del estudiante: ")

        if name.strip() == "":
            print("❌ Error: el nombre no puede estar vacío.")
        elif name.isdigit():
            print("❌ Error: el nombre no puede ser solo números.")
        else:
            break

    # VALIDACIÓN DE NOTAS
    grades = []

    for i in range(3):
        while True:
            try:
                grade = float(input(f"Ingrese nota {i + 1} (0-10): "))

                if 0 <= grade <= 10:
                    grades.append(grade)
                    break
                else:
                    print("❌ Error: la nota debe estar entre 0 y 10.")
            except ValueError:
                print("❌ Error: debe ingresar un número válido.")

    student = Student(name)
    student.show_average(grades)
