class Product:
    def __init__(self, code, name, price):

        if price < 0:
            raise ValueError("El precio no puede ser negativo")

        self.code = code
        self.name = name
        self.price = price


def run():
    print("=== REGISTRO DE PRODUCTOS FIJOS ===\n")

    try:
        # Producto 1
        product1 = Product("P001", "Laptop", 1200)

        # Producto 2
        product2 = Product("P002", "Mouse", 30)

        print("=== PRODUCTOS REGISTRADOS ===")
        print(product1.code, product1.name, product1.price)
        print(product2.code, product2.name, product2.price)

    except ValueError as e:
        print("❌ Error:", e)
