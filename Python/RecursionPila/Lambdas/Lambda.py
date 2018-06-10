def compara(num):
    if isinstance(num, int):
        entre0y4 = lambda digito : digito <= 4
        entre5y9 = lambda digito : digito >= 5
        return compara_aux(num, entre0y4), compara_aux(num, entre5y9)
    else:
        return -1

def compara_aux(num, condicion):
    if (num == 0):
        return 0
    elif condicion(num % 10):
        return 1 + compara_aux(num//10, condicion)
    else:
        return compara_aux(num//10, condicion)
