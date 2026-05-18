import json


class ExportarMixin:
    def exportar_json(self, datos):
        return json.dumps(datos, indent=2)

    def exportar_csv(self, datos):
        return ",".join(str(d) for d in datos)


class Reporte(ExportarMixin):
    def mostrar_exportaciones(self, datos):
        print("\n--- JSON ---")
        print(self.exportar_json(datos))

        print("\n--- CSV ---")
        print(self.exportar_csv(datos))


def ejecutar():

    print("📦 Registro de productos")

    productos = []

    # 🔹 VALIDACIÓN DE CANTIDAD
    while True:
        try:
            cantidad = int(input("¿Cuántos productos deseas ingresar?: "))

            if cantidad <= 0:
                print("❌ Debes ingresar un número mayor a 0")
            else:
                break

        except ValueError:
            print("❌ Debes ingresar un número entero válido")

    # 🔹 INGRESO DE PRODUCTOS
    for i in range(cantidad):

        print(f"\nProducto {i + 1}")

        # Validar nombre
        while True:
            nombre = input("Nombre del producto: ").strip()
            if nombre == "":
                print("❌ El nombre no puede estar vacío")
            else:
                break

        # Validar precio
        while True:
            try:
                precio = float(input("Precio del producto: "))
                if precio < 0:
                    print("❌ El precio no puede ser negativo")
                else:
                    break
            except ValueError:
                print("❌ Debes ingresar un número válido")

        productos.append({
            "nombre": nombre,
            "precio": precio
        })

    # 🔹 EXPORTAR
    reporte = Reporte()
    reporte.mostrar_exportaciones(productos)

