def multid(digi, num):
    if isinstance(num, int) and (num > 0) and (digi, int) and (num > 0):
        return multid_aux(digi, num)
    else:
        return -1

def multid_aux(digi, num):
    if (num == 0):
        return []
    elif ((digi * (num%10)) < 9):
        return [digi * (num%10)] + multid_aux(digi , num//10)
    else:
        return multid_aux(digi, num//10)
