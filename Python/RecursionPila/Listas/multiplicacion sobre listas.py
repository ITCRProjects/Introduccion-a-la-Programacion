def multiplicaciones(lista):
    if isinstance(lista,list) and (lista != []):
        return multiplicaciones_aux(lista, 0)
    else:
        return "Error: el valor ingresado no es una lista"

def multiplicaciones_aux(lista, contador):
    if (lista == []):
        return lista
    else:
        return [lista[0] * contador] + multiplicaciones_aux(lista[1:], contador + 1)
