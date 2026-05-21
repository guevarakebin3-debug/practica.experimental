def run():

    print("Decorador simple")

    def decorator(func):
        def wrapper():
            print("Iniciando...")
            func()
        return wrapper


    @decorator
    def greet():
        print("Hola mundo")

    greet()


    print("Decorador para calcular el cuadrado con validación")

    def validate_positive(func):
        def wrapper(n):
            try:
                if n < 0:
                    print("❌ Error: el número debe ser positivo")
                    return None
                return func(n)
            except Exception as e:
                print("❌ Ocurrió un error:", e)
                return None
        return wrapper


    @validate_positive
    def square(n):
        return n ** 2


    try:
        num = int(input("Ingrese un número: "))
        result = square(num)
        print("Resultado:", result)

    except ValueError:
        print("❌ Error: debes ingresar un número válido")
