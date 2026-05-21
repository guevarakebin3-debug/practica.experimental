class Product:
    def __init__(self, code, name, price):

        if price < 0:
            raise ValueError("El precio no puede ser negativo")

        self.code = code
        self.name = name
        self.price = price


def ask_price(product_name):
    while True:
        try:
            price = float(input(f"Ingrese el precio de{product_name}: "))
            if price < 0:
                raise ValueError("El precio no puede ser negativo")
            return price
        except ValueError as e:
            print("❌ Error:", e)


def run():
    print("=== REGISTRO DE PRODUCTOS FIJOS ===\n")

    # Product 1
    code1, name1 = "P001", "Laptop"
    print(f"Product: {code1} - {name1}")

    price1 = ask_price(name1)
    product1 = Product(code1, name1, price1)

    print()

    # Product 2
    code2, name2 = "P002", "Mouse"
    print(f"Product: {code2} - {name2}")

    price2 = ask_price(name2)
    product2 = Product(code2, name2, price2)

    print("\n=== REGISTERED PRODUCTS ===")
    print(product1.code, product1.name, product1.price)
    print(product2.code, product2.name, product2.price)
