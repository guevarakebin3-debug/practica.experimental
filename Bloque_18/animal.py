class Animal:
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print("El perro ladra")


class Cat(Animal):
    def sound(self):
        print("El gato maúlla")


class Cow(Animal):
    def sound(self):
        print("La vaca muge")


def run():
    animals = [Dog(), Cat(), Cow()]

    for animal in animals:
        animal.sound()
