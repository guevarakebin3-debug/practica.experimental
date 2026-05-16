def ejecutar():

    print("Bloque 13")

    print("Ejercicio 1 - Decorador simple")

    def decorador(func):
        def wrapper():
            print("Iniciando...")
            func()
        return wrapper


    @decorador
    def saludar():
        print("Hola mundo")

    saludar()


    print("\nEjercicio 2 - Decorador con validación")

    def validar_positivo(func):
        def wrapper(n):
            try:
                if n < 0:
                    print("Error: el número debe ser positivo")
                    return None
                return func(n)
            except Exception as e:
                print("Ocurrió un error:", e)
                return None
        return wrapper


    @validar_positivo
    def cuadrado(n):
        return n ** 2


    try:
        num = int(input("Ingrese un número: "))
        resultado = cuadrado(num)
        print("Resultado:", resultado)

    except ValueError:
        print("Error: debes ingresar un número válido")


    print("\nEjercicio 3 - Decorador log")

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
