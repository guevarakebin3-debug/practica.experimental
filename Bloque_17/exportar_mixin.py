import json


class ExportMixin:
    def export_json(self, data):
        return json.dumps(data, indent=2)

    def export_csv(self, data):
        return ",".join(str(d) for d in data)


class Report:
    def __init__(self):
        self.mixin = ExportMixin()

    def show_exports(self, data):
        print("\n--- JSON ---")
        print(self.mixin.export_json(data))

        print("\n--- CSV ---")
        print(self.mixin.export_csv(data))


def run():

    print("Registro de productos")

    products = []

    # VALIDACIÓN DE CANTIDAD
    while True:
        try:
            quantity = int(input("¿Cuántos productos deseas ingresar?: "))

            if quantity <= 0:
                print("Debes ingresar un número mayor a 0")
            else:
                break

        except ValueError:
            print("Debes ingresar un número entero válido")

    # INGRESO DE PRODUCTOS
    for i in range(quantity):

        print(f"\nProducto {i + 1}")

        # Validar nombre
        while True:
            name = input("Nombre del producto: ").strip()
            if name == "":
                print("El nombre no puede estar vacío")
            else:
                break

        # Validar precio
        while True:
            try:
                price = float(input("Precio del producto: "))
                if price < 0:
                    print("El precio no puede ser negativo")
                else:
                    break
            except ValueError:
                print("Debes ingresar un número válido")

        products.append({
            "nombre": name,
            "precio": price
        })

    # EXPORTAR
    report = Report()
    report.show_exports(products)
