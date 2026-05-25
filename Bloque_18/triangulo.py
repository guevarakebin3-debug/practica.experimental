from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return (self.base * self.height) / 2


def run():
    print("Descripción: Crear una clase abstracta Shape y una clase Triangle que implemente el método area().\n")

    t = Triangle(10, 5)

    print("DATOS DEL TRIÁNGULO:")
    print("Base:", t.base)
    print("Altura:", t.height)
    print("El área del triángulo es:", t.area())
