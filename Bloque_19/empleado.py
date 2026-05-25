
class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Employee(Person):
    def __init__(self, id, name, salary):
        super().__init__(id, name)
        self.salary = salary


def run():

    print("Crear una clase Persona y una clase Empleado que hereda de Persona.\n")

    employee = Employee("E01", "Carlos", 500)

    print("DATOS DEL EMPLEADO:")
    print("Nombre:", employee.name)
    print("Salario:", employee.salary)
