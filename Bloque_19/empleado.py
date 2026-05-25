
class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Employee(Person):
    def __init__(self, id, name, salary):
        super().__init__(id, name)
        self.salary = salary


def run():
    employee = Employee("E01", "Carlos", 500)

    print("Empleado:", employee.name)
    print("Salario:", employee.salary)

