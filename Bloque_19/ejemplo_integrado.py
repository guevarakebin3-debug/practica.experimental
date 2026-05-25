from abc import ABC, abstractmethod

# INTERFACE
class ICrud(ABC):
    @abstractmethod
    def create(self):
        pass


# ASSOCIATION
class Company:
    def __init__(self, name):
        self.business_name = name


# BASE CLASS
class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name


# INHERITANCE
class Client(Person):
    def __init__(self, id, name, email):
        super().__init__(id, name)
        self.email = email


class Product:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price


# COMPOSITION
class SaleDetail:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def subtotal(self):
        return self.product.price * self.quantity


# AGGREGATION + INTERFACE
class Sale(ICrud):
    def __init__(self, client):
        self.client = client
        self.details = []

    def add_product(self, product, quantity):
        self.details.append(SaleDetail(product, quantity))

    def create(self, company):
        print("Empresa:", company.business_name)
        print("Venta creada")

    def total(self):
        return sum(d.subtotal() for d in self.details)


def run():
    client = Client("001", "Daniel", "d@mail.com")

    p1 = Product("P01", "Laptop", 900)
    p2 = Product("P02", "Mouse", 25)

    sale = Sale(client)
    sale.add_product(p1, 1)
    sale.add_product(p2, 2)

    company = Company("SuperMaxi")

    sale.create(company)

    print("Cliente:", sale.client.name)
    print("Total:", sale.total())


if __name__ == "__main__":
    run()
