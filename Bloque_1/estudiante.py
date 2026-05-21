class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades if grades is not None else []

    @classmethod
    def from_dictionary(cls, data):
        return cls(
            data.get("nombre", ""),
            data.get("grades", [])
        )


def ask_student():
    name = input("Nombre: ").strip()

    entry = input("Notas (separadas por espacio): ").strip()
    grades = list(map(float, entry.split())) if entry else []

    return name, grades


def run():
    print("Crear estudiante)
    name, grades = ask_student()
    student = Student(name, grades)

    print("Resultado:")
    print(student.name, student.grades)

    print("\nCrear estudiante desde diccionario")

    name, grades = ask_student()

    data = {
        "name": name,
        "grades": grades
    }

    student2 = Student.from_dictionary(data)

    print("Resultado:")
    print(student2.name, student2.grades)
