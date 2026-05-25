class Product:
    def __init__(self, price=0):
        self.__price = 0
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("El precio no puede ser negativo")
        self.__price = value


def run():

    print("Descripción: Crear una clase Product que controle el acceso al atributo price usando property.\n")

    p = Product()
    p.price = 100

    print("DATOS DEL PRODUCTO:")
    print("El precio del producto es:", p.price)
