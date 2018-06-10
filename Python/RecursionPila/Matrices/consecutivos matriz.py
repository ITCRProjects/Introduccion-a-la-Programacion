def consecutivos(matriz):
    if isinstance(matriz, list) and (len(matriz) == len(matriz[0])):
        return auxiliar(matriz, len(matriz), len(matriz), 0, 1, 0)
    else:
        return -1

def auxiliar(matriz, largo, n, fila, contador, corrida):
    if (contador == n**2):
        return True
    elif (contador == matriz[fila][fila]):
        return auxiliar(matriz, largo, n, fila, contador + 1, corrida)
    else:
        return auxiliar(matriz, largo, n, fila + 1, contador, corrida + matriz[fila][fila])
