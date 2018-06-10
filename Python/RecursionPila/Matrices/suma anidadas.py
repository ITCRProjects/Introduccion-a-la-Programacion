def sumar(lista):
    if isinstance(lista, list) and (lista != []):
        return sumar_aux(lista)
    else:
        return "El valor ingresado no es de tipo lista"
    
def sumar_aux(lista):
    if (lista == []):
        return 0
    elif isinstance(lista[0], list):
        return sumar_aux(lista[0] + lista[1:])
    else:
        return lista[0] + sumar_aux(lista[1:])
