def ejecutar():

    print("Decorador de registro (log de ejecución)")

    def log(func):
        def wrapper(*args, **kwargs):
            print(" Iniciando ejecución de la función...")
            resultado = func(*args, **kwargs)
            print("Ejecución finalizada")
            return resultado
        return wrapper


    @log
    def suma(a, b):
        return a + b


    print("Resultado:", suma(2, 3))


    print("Decorador con entrada interactiva y multiplicación")

    def decorador(func):
        def wrapper(*args, **kwargs):
            print("Antes de ejecutar la función")
            resultado = func(*args, **kwargs)
            print("Después de ejecutar la función")
            return resultado
        return wrapper


    @decorador
    def multiplicar(a, b):
        return a * b


    # 🔥 VALIDACIÓN AQUÍ
    while True:
        try:
            a = int(input("Ingrese el primer número: "))
            b = int(input("Ingrese el segundo número: "))

            resultado = multiplicar(a, b)
            print("Resultado:", resultado)
            break

        except ValueError:
            print(" Error: debe ingresar números válidos")
