
def busqueda_binaria(elemento, lista):
    if isinstance(elemento, int) and isinstance(lista, list):
        return binaria_aux(elemento, lista, 0, (0 + (len(lista) - 1)) // 2, len(lista) - 1)

    else:
        return "Error"


def binaria_aux(elemento, lista, inicio, mitad, final):
    if elemento == lista[mitad]:
        return mitad

    elif elemento < lista[mitad]:
        return binaria_aux(elemento, lista, inicio, (inicio + final) // 2, mitad - 1)

    elif elemento > lista[mitad]:
        return binaria_aux(elemento, lista, mitad + 1, (inicio + final) // 2, final)
