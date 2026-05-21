class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return f"Name: {self.name} | Age: {self.age}"


def run():

    print("Create a Person class and three objects.\n")

    person1 = Person("Carlos", 20)
    person2 = Person("Ana", 25)
    person3 = Person("Luis", 30)

    print("Registered data:")

    print(person1.show())
    print(person2.show())
    print(person3.show())
