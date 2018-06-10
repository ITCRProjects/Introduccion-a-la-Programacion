def estadisticas(matriz):
    if isinstance(matriz, list) and (len(matriz) == len(matriz[0])):
        return promedio(matriz, len(matriz), len(matriz[0]), 0, 0, 0)
    else:
        return -1

def promedio(matriz, largof, largoc, fila, columna, suma):
    if (columna == largoc):
        return suma
    else:
        return promedio(matriz, largof, largoc, fila + 1, columna + 1, suma + matriz[fila][columna]// largof)
