def run():
    
    print("Incrementa en 1 cada elemento de la lista usando map")

    numbers = [2, 4, 6]

    result = list(map(lambda x: x + 1, numbers))

    print("Lista original:", numbers)
    print("Resultado:", result)
