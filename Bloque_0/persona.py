class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar(self):
        return f"Nombre: {self.nombre} | Edad: {self.edad}"


def ejecutar():

    print("Descripción:")
    print("Crear una clase Persona y tres objetos.\n")

    persona1 = Persona("Carlos", 20)
    persona2 = Persona("Ana", 25)
    persona3 = Persona("Luis", 30)

    print("Datos registrados:")
    print(persona1.mostrar())
    print(persona2.mostrar())
    print(persona3.mostrar())
