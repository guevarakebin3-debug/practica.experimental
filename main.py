# main.py

import os
import importlib

from menu import mostrar_menu


# =========================================
# EJECUTAR ARCHIVO
# =========================================

def ejecutar_archivo(modulo):

    try:

        archivo = importlib.import_module(modulo)

        if hasattr(archivo, "ejecutar"):
            archivo.ejecutar()
        else:
            print("\n⚠ El archivo no tiene función ejecutar()")

    except Exception as e:
        print(f"\n❌ Error: {e}")


# =========================================
# CREAR SUBMENU DE BLOQUE
# =========================================

def crear_submenu(nombre_bloque):

    ruta = os.path.join(os.getcwd(), nombre_bloque)

    archivos = os.listdir(ruta)

    opciones = {}

    contador = 1

    for archivo in archivos:

        if archivo.endswith(".py") and archivo != "__init__.py":

            nombre_archivo = archivo[:-3]

            modulo = f"{nombre_bloque}.{nombre_archivo}"

            opciones[str(contador)] = {
                "texto": nombre_archivo,
                "accion": lambda m=modulo: ejecutar_archivo(m)
            }

            contador += 1

    opciones["0"] = {
        "texto": "Volver",
        "accion": None
    }

    mostrar_menu(nombre_bloque.upper(), opciones)


# =========================================
# MENU PRINCIPAL
# =========================================

def menu_principal():

    carpetas = os.listdir()

    opciones = {}

    contador = 1

    for carpeta in carpetas:

        if carpeta.startswith("Bloque_") and os.path.isdir(carpeta):

            opciones[str(contador)] = {
                "texto": carpeta,
                "accion": lambda c=carpeta: crear_submenu(c)
            }

            contador += 1

    opciones["0"] = {
        "texto": "Salir",
        "accion": None
    }

    mostrar_menu("MENU PRINCIPAL", opciones)


# =========================================
# INICIO
# =========================================

menu_principal()
