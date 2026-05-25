from abc import ABC, abstractmethod


# INTERFACE
class ICrud(ABC):
    @abstractmethod
    def crear(self):
        pass


# ASSOCIATION
class Empresa:
    def __init__(self, nombre):
        self.razonsocial = nombre


# BASE CLASS
class Persona:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre


# HERENCIA
class Cliente(Persona):
    def __init__(self, id, nombre, correo):
        super().__init__(id, nombre)
        self.correo = correo


class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio


# COMPOSITION
class DetalleVenta:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

    def subtotal(self):
        return self.producto.precio * self.cantidad


# AGGREGATION + INTERFACE
class Venta(ICrud):
    def __init__(self, cliente):
        self.cliente = cliente
        self.detalles = []

    def agregar(self, producto, cantidad):
        self.detalles.append(DetalleVenta(producto, cantidad))

    def crear(self, emp):
        print("Empresa:", emp.razonsocial)
        print("Venta creada")

    def total(self):
        return sum(d.subtotal() for d in self.detalles)


# FUNCIÓN PRINCIPAL
def run():

    print("\n=== RELACIONES UML ===\n")

    print("1. Herencia")
    print("Cliente → Persona = Cliente ES UNA Persona")

    print("\n2. Interfaz")
    print("Venta → ICrud = Venta implementa un contrato")

    print("\n3. Asociación")
    print("Venta → Empresa = Venta usa Empresa como parámetro")

    print("\n4. Agregación")
    print("Venta → Cliente = Venta tiene un cliente externo")

    print("\n5. Composición")
    print("Venta → DetalleVenta = Venta crea y controla los detalles")


