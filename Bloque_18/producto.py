class Product:
    def __init__(self, price=0):
        self.__price = 0
        self.price = price  # usa el setter

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("El precio no puede ser negativo")
        self.__price = value


p = Product()
p.price = 100

print("El precio del producto es:", p.price)  # salida en español

# p.price = -5  -> Error: El precio no puede ser negativo
