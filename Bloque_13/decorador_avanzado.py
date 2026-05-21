def run():

    print("Decorador de registro (log de ejecución)")

    def log(func):
        def wrapper(*args, **kwargs):
            print("Iniciando ejecución de la función...")
            result = func(*args, **kwargs)
            print("Ejecución finalizada")
            return result
        return wrapper


    @log
    def add(a, b):
        return a + b


    print("Resultado:", add(2, 3))


    print("Decorador con entrada interactiva y multiplicación")

    def decorator(func):
        def wrapper(*args, **kwargs):
            print("Antes de ejecutar la función")
            result = func(*args, **kwargs)
            print("Después de ejecutar la función")
            return result
        return wrapper


    @decorator
    def multiply(a, b):
        return a * b


    # 🔥 VALIDACIÓN AQUÍ
    while True:
        try:
            a = int(input("Ingrese el primer número: "))
            b = int(input("Ingrese el segundo número: "))

            result = multiply(a, b)
            print("Resultado:", result)
            break

        except ValueError:
            print("❌ Error: debe ingresar números válidos")
