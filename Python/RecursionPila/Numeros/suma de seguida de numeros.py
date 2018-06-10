def summ(num):
    if isinstance(num, int) and (num > 0):
        return summ_aux(num, 0)
    else:
        return "Error: La entrada no es de tipo lista"

def mult_aux(j, z):
    if (z == j + 1):
        return 1
    else:
        return ((3 * z ** 2) - z) * mult_aux(j, z + 1)

def summ_aux(num, j):
    if (j == num):
        return 0
    else:
        return  mult_aux(j + 1, 1) + summ_aux(num, j + 1)
