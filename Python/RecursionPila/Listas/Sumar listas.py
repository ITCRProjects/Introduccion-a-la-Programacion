def suma(lista):
    if isinstance(lista, list):
        return suma_aux(lista)
    else:
        return "Error: La entrada no es una lista."

def suma_aux(lista):
    if (lista == []):
        return 0
    elif isinstance(lista[0], list):
        return  suma_aux(lista[0]) + suma_aux(lista[1:])
    else:
        return lista[0] + suma_aux(lista[1:])
