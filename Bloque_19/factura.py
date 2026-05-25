class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# COMPOSICION
class InvoiceDetail:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def subtotal(self):
        return self.product.price * self.quantity


# MAIN CLASS
class Invoice:
    def __init__(self):
        self.details = []

    def add_product(self, product, quantity):
        self.details.append(InvoiceDetail(product, quantity))

    def total(self):
        return sum(d.subtotal() for d in self.details)


def run():

    print(" Crear una factura que almacene productos, cantidades y calcule el total.\n")

    p1 = Product("Teclado", 30)
    p2 = Product("Monitor", 200)

    invoice = Invoice()
    invoice.add_product(p1, 2)
    invoice.add_product(p2, 1)

    print("DETALLE DE FACTURA:")
    print("- Teclado x2 = 60")
    print("- Monitor x1 = 200")

    print("\nTOTAL DE LA FACTURA:", invoice.total())

