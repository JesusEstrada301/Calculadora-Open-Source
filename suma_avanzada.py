def suma_avanzada():
    arr = []
    total = 0
    bandera = 1
    num = int(input("¿Que valor desea sumar? \n"))
    arr.append(num)
    while bandera == 1:
        num = int(input("¿Que valor desea sumar? \n"))
        arr.append(num)
        respuesta = input("¿Desea agregar mas? (y/n) \n")
        if respuesta == "n":
            bandera = 0
    for i in arr:
        total += i
    return total