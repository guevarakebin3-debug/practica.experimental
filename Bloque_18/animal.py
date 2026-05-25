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

    print("Crea una clase Animal y varias clases hijas que implementan su propio sonido.\n")

    animals = [Dog(), Cat(), Cow()]

    print("SONIDOS DE LOS ANIMALES:")

    for animal in animals:
        animal.sound()
