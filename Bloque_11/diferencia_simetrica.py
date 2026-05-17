def ejecutar():

    print("Ejercicio 3")
    print("Diferencia simétrica")
    
    A = {1, 2, 3, 4}
    B = {3, 4, 5, 6}

    resultado = (A | B) - (A & B)

    print("Conjunto A:", A)
    print("Conjunto B:", B)
    print("Resultado:", resultado)
    
print("\nEjercicio adicional")
print("Operaciones completas entre conjuntos")

A = set()
B = set()

# Validar cantidad A
while True:
    try:
        cantidad_a = int(input("¿Cuántos números tendrá el conjunto A?: "))
        if cantidad_a < 0:
            print("❌ No puede ser negativo")
        else:
            break
    except ValueError:
        print("❌ Debe ingresar un número entero")

# Llenar A
for i in range(cantidad_a):

    while True:
        try:
            num = int(input(f"Ingrese número {i + 1} para A: "))
            A.add(num)
            break
        except ValueError:
            print("❌ Debe ingresar un número entero")

# Validar cantidad B
while True:
    try:
        cantidad_b = int(input("\n¿Cuántos números tendrá el conjunto B?: "))
        if cantidad_b < 0:
            print("❌ No puede ser negativo")
        else:
            break
    except ValueError:
        print("❌ Debe ingresar un número entero")

# Llenar B
for i in range(cantidad_b):

    while True:
        try:
            num = int(input(f"Ingrese número {i + 1} para B: "))
            B.add(num)
            break
        except ValueError:
            print("❌ Debe ingresar un número entero")

print("\nConjunto A:", A)
print("Conjunto B:", B)

print("\nUnión:", A | B)
print("Intersección:", A & B)
print("Diferencia (A - B):", A - B)
print("Diferencia simétrica:", A ^ B)
