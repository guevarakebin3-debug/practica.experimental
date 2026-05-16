from menu import mostrar_menu
from Bloque_0.persona import ejecutar as persona 
from Bloque_1.producto import ejecutar as producto
from Bloque_1.estudiante import ejecutar as estudiante
from Bloque_2.tipos_datos import ejecutar as tipos
from Bloque_2.clases_objetos import ejecutar as listas
from Bloque_3.operadores_aritmeticos import ejecutar as operadores
from Bloque_4.entrada_datos import ejecutar as entrada
from Bloque_4.promedio_numeros import ejecutar as promedio
from Bloque_4.concatenacion_texto import ejecutar as concat
from Bloque_5.par_impar import ejecutar as par
from Bloque_5.notas import ejecutar as notas
from Bloque_5.login import ejecutar as login
from Bloque_6.ciclos import ejecutar as ciclos







# FUNCIONES DE EJEMPLO
# (luego aquí conectas tus archivos reales)
# =========================

def ejecutar_bloque(nombre):
    print(f"\nEjecutando {nombre}")


# =========================
# SUBMENÚS
# =========================

def crear_menu_bloque(nombre_bloque, ejercicios):

    opciones = {}

    contador = 1

    for e in ejercicios:

        opciones[str(contador)] = {
            "texto": e,
            "accion": lambda n=f"{nombre_bloque} -> {e}": ejecutar_bloque(n)
        }

        contador += 1

    opciones["0"] = {
        "texto": "Volver",
        "accion": None
    }

    mostrar_menu(nombre_bloque, opciones)


# =========================
# BLOQUES (DEL 0 AL 17)
# =========================

def menu_bloque_0():

    opciones = {

        "1": {
            "texto": "Persona",
            "accion": persona
        },

        "0": {
            "texto": "Volver",
            "accion": None
        }
    }

    mostrar_menu("BLOQUE 0", opciones)
   

def menu_bloque_1():

    opciones = {

        "1": {
            "texto": "Producto",
            "accion": producto
        },

        "2": {
            "texto": "Estudiante",
            "accion": estudiante
        },

        "0": {
            "texto": "Volver",
            "accion": None
        }
    }

    mostrar_menu("BLOQUE 1", opciones)

def menu_bloque_2():

    opciones = {

        "1": {
            "texto": "Tipos de datos",
            "accion": tipos
        },

        "2": {
            "texto": "Listas",
            "accion": listas
        },

        "0": {
            "texto": "Volver",
            "accion": None
        }
    }

    mostrar_menu("BLOQUE 2", opciones)


def menu_bloque_3():

    opciones = {

        "1": {
            "texto": "Operadores",
            "accion": operadores
        },

        "0": {
            "texto": "Volver",
            "accion": None
        }
    }

    mostrar_menu("BLOQUE 3", opciones)


def menu_bloque_4():
    crear_menu_bloque("BLOQUE 4", ["ejercicio1"])

def menu_bloque_5():

    opciones = {

        "1": {
            "texto": "Par o impar",
            "accion": par
        },

        "2": {
            "texto": "Notas",
            "accion": notas
        },

        "3": {
            "texto": "Login",
            "accion": login
        },

        "0": {
            "texto": "Volver",
            "accion": None
        }
    }

    mostrar_menu("BLOQUE 5", opciones)

def menu_bloque_6():

    opciones = {

        "1": {
            "texto": "Ciclos",
            "accion": ciclos
        },

        "0": {
            "texto": "Volver",
            "accion": None
        }
    }

    mostrar_menu("BLOQUE 6", opciones)

def menu_bloque_7():
    crear_menu_bloque("BLOQUE 7", ["ejercicio1"])


def menu_bloque_8():
    crear_menu_bloque("BLOQUE 8", ["ejercicio1"])


def menu_bloque_9():
    crear_menu_bloque("BLOQUE 9", ["ejercicio1"])


def menu_bloque_10():
    crear_menu_bloque("BLOQUE 10", ["ejercicio1"])


def menu_bloque_11():
    crear_menu_bloque("BLOQUE 11", ["ejercicio1"])


def menu_bloque_12():
    crear_menu_bloque("BLOQUE 12", ["ejercicio1"])


def menu_bloque_13():
    crear_menu_bloque("BLOQUE 13", ["ejercicio1"])


def menu_bloque_14():
    crear_menu_bloque("BLOQUE 14", ["ejercicio1"])


def menu_bloque_15():
    crear_menu_bloque("BLOQUE 15", ["ejercicio1"])


def menu_bloque_16():
    crear_menu_bloque("BLOQUE 16", ["ejercicio1"])


def menu_bloque_17():
    crear_menu_bloque("BLOQUE 17", ["ejercicio1"])


# =========================
# MENU PRINCIPAL
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


# =========================
# INICIO
# =========================

menu_principal()
