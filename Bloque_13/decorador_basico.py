def ejecutar():

    print("Decorador simple")

    def decorador(func):
        def wrapper():
            print("Iniciando...")
            func()
        return wrapper


    @decorador
    def saludar():
        print("Hola mundo")

    saludar()


    print(" Decorador para calcular el cuadrado con validación")

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
