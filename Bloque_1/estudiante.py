class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades if grades is not None else []

    @classmethod
    def from_dictionary(cls, data):
        return cls(
            data.get("name", ""),
            data.get("grades", [])
        )


def run():
    # Un solo estudiante con datos fijos
    data = {
        "name": "Carlos",
        "grades": [9.5, 8.7, 10]
    }

    student = Student.from_dictionary(data)

    print("Resultado:")
    print(student.name, student.grades)
