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

    print("Bloque 17 - ExportarMixin")

    datos = []

    cantidad = int(input("¿Cuántos datos deseas ingresar?: "))

    for i in range(cantidad):
        dato = input(f"Ingrese dato {i + 1}: ")
        datos.append(dato)

    reporte = Reporte()
    reporte.mostrar_exportaciones(datos)
