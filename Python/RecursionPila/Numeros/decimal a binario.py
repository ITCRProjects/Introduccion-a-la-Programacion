def convertir(num):
    if isinstance(num, float):
        return entero(int(num)), fraccion(num- int(num))
    else:
        return -1

def entero(entero):
    if isinstance(entero, int) and (entero >= 0):
        if (entero == 1 or entero == 0):
            return [entero]
        else:
            return dec_bin_aux(entero)
    else:
        return "Error el valor ingresado no es un numero"

def dec_bin_aux(decimal):
    if (decimal == 0):
        return []
    else:
        return dec_bin_aux(decimal//2) + [decimal % 2]

def fraccion(fraccion):
    if isinstance(fraccion, float) and (fraccion > 0):
        return fra_bin_aux(fraccion)
    else:
        return []

def fra_bin_aux(fraccion):
    if (fraccion == 0.0):
        return[]
    else:
        return [int(fraccion * 2)] + fra_bin_aux((fraccion * 2) - int(fraccion * 2))
