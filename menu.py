from consoleUtils import ConsoleUtils


# =========================
# COMPATIBILIDAD
# =========================

def limpiar():
    ConsoleUtils.clear_screen()


def gotoxy(x, y):
    ConsoleUtils.gotoxy(x, y)

# =========================
# IMPORTS DE BLOQUES
# =========================

from Bloque_0.persona import ejecutar as persona
from Bloque_1.producto import ejecutar as producto
from Bloque_1.estudiante import ejecutar as estudiante
from Bloque_2.tipos_datos import ejecutar as tipos
from Bloque_2.clases_objetos import ejecutar as clases_objetos
from Bloque_3.operadores_aritmeticos import ejecutar as operadores
from Bloque_4.entrada_datos import ejecutar as entrada
from Bloque_4.promedio_numeros import ejecutar as promedio
from Bloque_4.concatenacion_texto import ejecutar as concat
from Bloque_5.par_impar import ejecutar as par
from Bloque_5.notas import ejecutar as notas
from Bloque_5.login import ejecutar as login
from Bloque_6.ciclos import ejecutar as ciclos
from Bloque_7.funciones import ejecutar as funciones
from Bloque_7.factorial import ejecutar as factorial
from Bloque_7.operaciones import ejecutar as operaciones
from Bloque_8.listas import ejecutar as lista
from Bloque_8.copiar_lista import ejecutar as copiar
from Bloque_9.tuplas import ejecutar as tuplas
from Bloque_9.coordenadas import ejecutar as coordenadas
from Bloque_10.diccionarios import ejecutar as diccionarios
from Bloque_10.copia_diccionario import ejecutar as copia_diccionario
from Bloque_11.conjuntos import ejecutar as conjuntos
from Bloque_11.duplicados import ejecutar as duplicados
from Bloque_11.diferencia_simetrica import ejecutar as diferencia_simetrica
from Bloque_12.value_error import ejecutar as value_error
from Bloque_12.index_error import ejecutar as index_error
from Bloque_12.division_error import ejecutar as division_error
from Bloque_12.actualizar_lista import ejecutar as actualizar_lista
from Bloque_13.decorador_basico import ejecutar as decorador_basico
from Bloque_13.decorador_avanzado import ejecutar as decorador_avanzado
from Bloque_14.listas_unpacking import ejecutar as listas_unpacking
from Bloque_14.diccionarios_unpacking import ejecutar as diccionarios_unpacking
from Bloque_14.unpacking_extra import ejecutar as unpacking_extra
from Bloque_15.map_lambda import ejecutar as map_lambda
from Bloque_15.filter_lambda import ejecutar as filter_lambda
from Bloque_15.reduce_lambda import ejecutar as reduce_lambda
from Bloque_16.archivos import ejecutar as archivos
from Bloque_16.json_datos import ejecutar as json_datos
from Bloque_17.promedio_mixin import ejecutar as promedio_mixin
from Bloque_17.validacion_mixin import ejecutar as validacion_mixin
from Bloque_17.exportar_mixin import ejecutar as exportar_mixin


# =========================
# MOSTRAR MENÚ
# =========================

# =========================
# MOSTRAR MENÚ
# =========================

# =========================
# MOSTRAR MENÚ
# =========================

def mostrar_menu(titulo, opciones):

    while True:

        ConsoleUtils.clear_screen()

        lineas = []

        # Construir opciones
        for clave, valor in opciones.items():
            lineas.append(
                f"{clave}. {valor['texto']}"
            )

        # Mostrar menú
        ConsoleUtils.print_box(
            titulo,
            lineas
        )

        opcion = input(
            "\nSeleccione una opción: "
        ).strip()

        if opcion in opciones:

            accion = opciones[opcion]["accion"]

            # Salir o volver
            if accion is None:
                break

            # Entrar al ejercicio
            ConsoleUtils.clear_screen()

            ConsoleUtils.print_box(
                "EJERCICIOS",
                []
            )

            accion()

            print()

            input("Presione ENTER para volver...")

        else:

            print("\n❌ Opción inválida")

            input("Presione ENTER...")
# =========================
# CREAR SUBMENÚ
# =========================

def crear_submenu(titulo, ejercicios):

    opciones = {}

    contador = 1

    for texto, accion in ejercicios:

        opciones[str(contador)] = {
            "texto": texto,
            "accion": accion
        }

        contador += 1

    opciones["0"] = {
        "texto": "Volver",
        "accion": None
    }

    mostrar_menu(titulo, opciones)


# =========================
# MENÚS DE BLOQUES
# =========================

def menu_bloque_0():
    crear_submenu("BLOQUE 0", [
        ("Persona", persona)
    ])


def menu_bloque_1():
    crear_submenu("BLOQUE 1", [
        ("Producto", producto),
        ("Estudiante", estudiante)
    ])


def menu_bloque_2():
    crear_submenu("BLOQUE 2", [
        ("Tipos de datos", tipos),
        ("Clases", clases_objetos)
    ])


def menu_bloque_3():
    crear_submenu("BLOQUE 3", [
        ("Operadores", operadores)
    ])


def menu_bloque_4():
    crear_submenu("BLOQUE 4", [
        ("Entrada", entrada),
        ("Promedio", promedio),
        ("Concatenación", concat)
    ])


def menu_bloque_5():
    crear_submenu("BLOQUE 5", [
        ("Par o impar", par),
        ("Notas", notas),
        ("Login", login)
    ])


def menu_bloque_6():
    crear_submenu("BLOQUE 6", [
        ("Ciclos", ciclos)
    ])


def menu_bloque_7():
    crear_submenu("BLOQUE 7", [
        ("Funciones", funciones),
        ("Factorial", factorial),
        ("Operaciones", operaciones)
    ])


def menu_bloque_8():
    crear_submenu("BLOQUE 8", [
        ("Listas", lista),
        ("Copiar listas", copiar)
    ])


def menu_bloque_9():
    crear_submenu("BLOQUE 9", [
        ("Tuplas", tuplas),
        ("Coordenadas", coordenadas)
    ])


def menu_bloque_10():
    crear_submenu("BLOQUE 10", [
        ("Diccionarios", diccionarios),
        ("Copia", copia_diccionario)
    ])


def menu_bloque_11():
    crear_submenu("BLOQUE 11", [
        ("Conjuntos", conjuntos),
        ("Duplicados", duplicados),
        ("Simétrica", diferencia_simetrica)
    ])


def menu_bloque_12():
    crear_submenu("BLOQUE 12", [
        ("ValueError", value_error),
        ("IndexError", index_error),
        ("División", division_error),
        ("Actualizar lista", actualizar_lista)
    ])


def menu_bloque_13():
    crear_submenu("BLOQUE 13", [
        ("Decorador básico", decorador_basico),
        ("Decorador avanzado", decorador_avanzado)
    ])


def menu_bloque_14():
    crear_submenu("BLOQUE 14", [
        ("Listas unpacking", listas_unpacking),
        ("Diccionarios unpacking", diccionarios_unpacking),
        ("Extra", unpacking_extra)
    ])


def menu_bloque_15():
    crear_submenu("BLOQUE 15", [
        ("Map", map_lambda),
        ("Filter", filter_lambda),
        ("Reduce", reduce_lambda)
    ])


def menu_bloque_16():
    crear_submenu("BLOQUE 16", [
        ("Archivos", archivos),
        ("JSON", json_datos)
    ])


def menu_bloque_17():
    crear_submenu("BLOQUE 17", [
        ("Promedio Mixin", promedio_mixin),
        ("Validación Mixin", validacion_mixin),
        ("Exportar Mixin", exportar_mixin)
    ])


# =========================
# MENÚ PRINCIPAL
# =========================

def menu_principal():

    opciones = {
        "1": {"texto": "Bloque 0", "accion": menu_bloque_0},
        "2": {"texto": "Bloque 1", "accion": menu_bloque_1},
        "3": {"texto": "Bloque 2", "accion": menu_bloque_2},
        "4": {"texto": "Bloque 3", "accion": menu_bloque_3},
        "5": {"texto": "Bloque 4", "accion": menu_bloque_4},
        "6": {"texto": "Bloque 5", "accion": menu_bloque_5},
        "7": {"texto": "Bloque 6", "accion": menu_bloque_6},
        "8": {"texto": "Bloque 7", "accion": menu_bloque_7},
        "9": {"texto": "Bloque 8", "accion": menu_bloque_8},
        "10": {"texto": "Bloque 9", "accion": menu_bloque_9},
        "11": {"texto": "Bloque 10", "accion": menu_bloque_10},
        "12": {"texto": "Bloque 11", "accion": menu_bloque_11},
        "13": {"texto": "Bloque 12", "accion": menu_bloque_12},
        "14": {"texto": "Bloque 13", "accion": menu_bloque_13},
        "15": {"texto": "Bloque 14", "accion": menu_bloque_14},
        "16": {"texto": "Bloque 15", "accion": menu_bloque_15},
        "17": {"texto": "Bloque 16", "accion": menu_bloque_16},
        "18": {"texto": "Bloque 17", "accion": menu_bloque_17},
        "0": {"texto": "Salir", "accion": None}
    }

    mostrar_menu("MENU PRINCIPAL", opciones)



