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


def ask_student():
    name = input("Name: ").strip()

    entry = input("Grades (separated by space): ").strip()
    grades = list(map(float, entry.split())) if entry else []

    return name, grades


def run():
    print("Create normal student")
    name, grades = ask_student()
    student = Student(name, grades)

    print("Result:")
    print(student.name, student.grades)

    print("\nCreate student from dictionary")

    name, grades = ask_student()

    data = {
        "name": name,
        "grades": grades
    }

    student2 = Student.from_dictionary(data)

    print("Result:")
    print(student2.name, student2.grades)
