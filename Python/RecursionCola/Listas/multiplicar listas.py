def mult(lista):
    if isinstance(lista, list):
        return mult_aux(lista, 1)
    else:
        return -1

def mult_aux(lista, resultado):
    if (lista == []):
        return resultado
    else:
        return mult_aux(lista[1:], resultado * lista[0])

def mult2(lista):
    if isinstance(lista, list):
        return mult2_aux(lista, 1)
    else:
        return -1

def mult2_aux(lista, resultado):
    if (lista == []):
        return resultado
    elif isinstance(lista[0], list):
        return mult2_aux(lista[0] + lista[1:], resultado)
    else:
        return mult2_aux(lista[1:], resultado * lista[0])
