class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return f"Name: {self.name} | Age: {self.age}"


def run():

    print(""Crear una clase Persona y tres objetos.\n")

    person1 = Person("Carlos", 20)
    person2 = Person("Ana", 25)
    person3 = Person("Luis", 30)

    print("Datos registrados:")

    print(person1.show())
    print(person2.show())
    print(person3.show())
