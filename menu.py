from consoleUtils import ConsoleUtils


# =========================
# COMPATIBILITY
# =========================

def limpiar():
    ConsoleUtils.clear_screen()


def gotoxy(x, y):
    ConsoleUtils.gotoxy(x, y)


# =========================
# IMPORTS DE BLOQUES
# =========================

from Bloque_0.persona import run as persona
from Bloque_1.producto import run as producto
from Bloque_1.estudiante import run as estudiante
from Bloque_2.tipos_datos import run as tipos
from Bloque_2.clases_objetos import run as clases_objetos
from Bloque_3.operadores_aritmeticos import run as operadores
from Bloque_4.entrada_datos import run as entrada
from Bloque_4.promedio_numeros import run as promedio
from Bloque_4.concatenacion_texto import run as concat
from Bloque_5.par_impar import run as par
from Bloque_5.notas import run as notas
from Bloque_5.login import run as login
from Bloque_6.ciclos import run as ciclos
from Bloque_7.funciones import run as funciones
from Bloque_7.factorial import run as factorial
from Bloque_7.operaciones import run as operaciones
from Bloque_8.listas import run as lista
from Bloque_8.copiar_lista import run as copiar
from Bloque_9.tuplas import run as tuplas
from Bloque_9.coordenadas import run as coordenadas
from Bloque_10.diccionarios import run as diccionarios
from Bloque_10.copia_diccionario import run as copia_diccionario
from Bloque_11.conjuntos import run as conjuntos
from Bloque_11.duplicados import run as duplicados
from Bloque_11.diferencia_simetrica import run as diferencia_simetrica
from Bloque_12.value_error import run as value_error
from Bloque_12.index_error import run as index_error
from Bloque_12.division_error import run as division_error
from Bloque_12.actualizar_lista import run as actualizar_lista
from Bloque_13.decorador_basico import run as decorador_basico
from Bloque_13.decorador_avanzado import run as decorador_avanzado
from Bloque_14.listas_unpacking import run as listas_unpacking
from Bloque_14.diccionarios_unpacking import run as diccionarios_unpacking
from Bloque_14.unpacking_extra import run as unpacking_extra
from Bloque_15.map_lambda import run as map_lambda
from Bloque_15.filter_lambda import run as filter_lambda
from Bloque_15.reduce_lambda import run as reduce_lambda
from Bloque_16.archivos import run as archivos
from Bloque_16.json_datos import run as json_datos
from Bloque_17.promedio_mixin import run as promedio_mixin
from Bloque_17.mixin import run as mixin
from Bloque_18.animal import run as animal
from Bloque_18.producto import run as productos
from Bloque_18.triangulo import run as triangulo
from Bloque_19.ejemplo_integrado import run as ejemplo
from Bloque_19.empleado import run as empleado
from Bloque_19.factura import run as factura

# =========================
# MENU SYSTEM
# =========================

def show_menu(title, options):

    while True:

        ConsoleUtils.clear_screen()

        lines = []

        for key, value in options.items():
            lines.append(f"{key}. {value['text']}")

        ConsoleUtils.print_box(title, lines)

        option = input("\nSeleccione una opción: ").strip()

        if option in options:

            action = options[option]["action"]

            if action is None:
                break

            ConsoleUtils.clear_screen()

            ConsoleUtils.print_box("EJERCICIOS", [])

            action()

            print()
            input("Presione ENTER para volver...")

        else:
            print("\n❌ Opción inválida")
            input("Presione ENTER...")


# =========================
# CREATE SUBMENU
# =========================

def create_submenu(title, exercises):

    options = {}
    counter = 1

    for text, action in exercises:

        options[str(counter)] = {
            "text": text,
            "action": action
        }

        counter += 1

    options["0"] = {
        "text": "Volver",
        "action": None
    }

    show_menu(title, options)


# =========================
# BLOCK MENUS
# =========================

def menu_block_0():
    create_submenu("BLOQUE 0", [
        ("Persona", persona)
    ])


def menu_block_1():
    create_submenu("BLOQUE 1", [
        ("Producto", producto),
        ("Estudiante", estudiante)
    ])


def menu_block_2():
    create_submenu("BLOQUE 2", [
        ("Tipos de datos", tipos),
        ("Clases", clases_objetos)
    ])


def menu_block_3():
    create_submenu("BLOQUE 3", [
        ("Operadores", operadores)
    ])


def menu_block_4():
    create_submenu("BLOQUE 4", [
        ("Entrada", entrada),
        ("Promedio", promedio),
        ("Concatenación", concat)
    ])


def menu_block_5():
    create_submenu("BLOQUE 5", [
        ("Par o impar", par),
        ("Notas", notas),
        ("Login", login)
    ])


def menu_block_6():
    create_submenu("BLOQUE 6", [
        ("Ciclos", ciclos)
    ])


def menu_block_7():
    create_submenu("BLOQUE 7", [
        ("Funciones", funciones),
        ("Factorial", factorial),
        ("Operaciones", operaciones)
    ])


def menu_block_8():
    create_submenu("BLOQUE 8", [
        ("Listas", lista),
        ("Copiar listas", copiar)
    ])


def menu_block_9():
    create_submenu("BLOQUE 9", [
        ("Tuplas", tuplas),
        ("Coordenadas", coordenadas)
    ])


def menu_block_10():
    create_submenu("BLOQUE 10", [
        ("Diccionarios", diccionarios),
        ("Copia", copia_diccionario)
    ])


def menu_block_11():
    create_submenu("BLOQUE 11", [
        ("Conjuntos", conjuntos),
        ("Duplicados", duplicados),
        ("Simétrica", diferencia_simetrica)
    ])


def menu_block_12():
    create_submenu("BLOQUE 12", [
        ("ValueError", value_error),
        ("IndexError", index_error),
        ("División", division_error),
        ("Actualizar lista", actualizar_lista)
    ])


def menu_block_13():
    create_submenu("BLOQUE 13", [
        ("Decorador básico", decorador_basico),
        ("Decorador avanzado", decorador_avanzado)
    ])


def menu_block_14():
    create_submenu("BLOQUE 14", [
        ("Listas unpacking", listas_unpacking),
        ("Diccionarios unpacking", diccionarios_unpacking),
        ("Extra", unpacking_extra)
    ])


def menu_block_15():
    create_submenu("BLOQUE 15", [
        ("Map", map_lambda),
        ("Filter", filter_lambda),
        ("Reduce", reduce_lambda)
    ])


def menu_block_16():
    create_submenu("BLOQUE 16", [
        ("Archivos", archivos),
        ("JSON", json_datos)
    ])


def menu_block_17():
    create_submenu("BLOQUE 17", [
        ("Promedio Mixin", promedio_mixin),
        ("Mixin", mixin)
    ])

def menu_block_18():
    create_submenu("BLOQUE 18", [
        ("Animal", animal),
        ("Producto", productos),
        ("Triangulo", triangulo)
    ])

def menu_block_19():
    create_submenu("BLOQUE 19", [
        ("Ejemplo Integrado", ejemplo),
        ("Empleado", empleado),
        ("Factura", factura)
    ])


# =========================
# MAIN MENU
# =========================

def menu_principal():

    options = {
        "1": {"text": "Bloque 0", "action": menu_block_0},
        "2": {"text": "Bloque 1", "action": menu_block_1},
        "3": {"text": "Bloque 2", "action": menu_block_2},
        "4": {"text": "Bloque 3", "action": menu_block_3},
        "5": {"text": "Bloque 4", "action": menu_block_4},
        "6": {"text": "Bloque 5", "action": menu_block_5},
        "7": {"text": "Bloque 6", "action": menu_block_6},
        "8": {"text": "Bloque 7", "action": menu_block_7},
        "9": {"text": "Bloque 8", "action": menu_block_8},
        "10": {"text": "Bloque 9", "action": menu_block_9},
        "11": {"text": "Bloque 10", "action": menu_block_10},
        "12": {"text": "Bloque 11", "action": menu_block_11},
        "13": {"text": "Bloque 12", "action": menu_block_12},
        "14": {"text": "Bloque 13", "action": menu_block_13},
        "15": {"text": "Bloque 14", "action": menu_block_14},
        "16": {"text": "Bloque 15", "action": menu_block_15},
        "17": {"text": "Bloque 16", "action": menu_block_16},
        "18": {"text": "Bloque 17", "action": menu_block_17},
        "19": {"text": "Bloque 18", "action": menu_block_18}, 
        "20": {"text": "Bloque 19", "action": menu_block_19} 
        "0": {"text": "Salir", "action": None}
    }

    show_menu("MENU PRINCIPAL", options)


