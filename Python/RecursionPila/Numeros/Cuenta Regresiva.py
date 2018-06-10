def regresiva(valor):
    print(valor)
    if (valor > 0):
        regresiva (valor - 1)
    elif (valor <= 0):
        return 0

def regresiva2(valor):
    print(valor, end = " ")
    if (valor <= 0):
        return 0
    else:
        regresiva2(valor - 1)
