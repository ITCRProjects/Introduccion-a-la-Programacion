def invertir(lista):
    if isinstance(lista, list) and (lista != []):
        return invertir_aux(lista, 0, len(lista)-1)
    else:
        return -1

def invertir_aux(lista, contador, indice):
    if (contador == len(lista)):
        return lista
    else:
        return invertir_aux([[lista[indice]] + lista], contador + 1, indice)
