def ejecutar():

    print("Bloque 13 - Decoradores avanzados")

    print("Ejercicio 3 - Decorador log")

    def log(func):
        def wrapper(*args, **kwargs):
            print("Ejecutando función...")
            resultado = func(*args, **kwargs)
            print("Función terminada")
            return resultado
        return wrapper


    @log
    def suma(a, b):
        return a + b


    print("Resultado:", suma(2, 3))


    print("\nEjercicio adicional - Decorador interactivo")

    def decorador(func):
        def wrapper(*args, **kwargs):
            print("Antes de la función")
            resultado = func(*args, **kwargs)
            print("Después de la función")
            return resultado
        return wrapper


    @decorador
    def multiplicar(a, b):
        return a * b


    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))

    print("Resultado:", multiplicar(a, b))
