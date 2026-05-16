class Producto:
    def __init__(self, codigo, nombre, precio):

        if precio < 0:
            raise ValueError("El precio no puede ser negativo")

        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio


def ejecutar():

    print("Ingrese los datos del producto 1")

    codigo1 = input("Código: ")
    nombre1 = input("Nombre: ")

    while True:
        try:
            precio1 = float(input("Precio: "))
            producto1 = Producto(codigo1, nombre1, precio1)
            break
        except ValueError:
            print("❌ Error: ingresa un número válido para el precio")

    print("\nIngrese los datos del producto 2")

    codigo2 = input("Código: ")
    nombre2 = input("Nombre: ")

    while True:
        try:
            precio2 = float(input("Precio: "))
            producto2 = Producto(codigo2, nombre2, precio2)
            break
        except ValueError:
            print("❌ Error: ingresa un número válido para el precio")

    print("\nProductos registrados:")
    print(producto1.codigo, producto1.nombre, producto1.precio)
    print(producto2.codigo, producto2.nombre, producto2.precio)
