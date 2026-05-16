# menu.py

def mostrar_menu(titulo, opciones):

    while True:

        print(f"\n========== {titulo} ==========")

        for clave, valor in opciones.items():
            print(f"{clave}. {valor['texto']}")

        opcion = input("\nSeleccione una opción: ")

        if opcion in opciones:

            accion = opciones[opcion]["accion"]

            if accion is None:
                break

            accion()

        else:
            print("\n❌ Opción inválida")



