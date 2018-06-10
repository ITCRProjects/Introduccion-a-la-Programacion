def divisores(num):
    if isinstance(num, int) and (num > 0):
        return divisores_aux(num, 2)
    else:
        return -1

def divisores_aux(num, contador):
    if (contador == num-1):
        return []
    elif ((num % contador)== 0):
        return [contador] + divisores_aux(num, contador + 1)
    else:
        return divisores_aux(num, contador + 1)
© 2018 GitHub, Inc.
