def suma(matriz):
    if isinstance(matriz, list) and (len(matriz) == len(matriz[0])):
        return (filas(matriz, len(matriz), len(matriz[0]), 0, 0, 0), columnas(matriz, len(matriz), len(matriz[0]), 0, 0, 0),
                antidiagonal(matriz, len(matriz), 0, 0), (filas(matriz, len(matriz), len(matriz[0]), 0, 0, 0) + columnas(matriz, len(matriz), len(matriz[0]), 0, 0, 0) +
                antidiagonal(matriz, len(matriz), 0, 0)))
    else:
        return -1

#Suma primera fila.
def filas(matriz, largof, largoc, fila, columna, suma):
    if (columna == largoc):
        return suma
    else:
        return filas(matriz, largof, largoc, fila, columna + 1, suma + matriz[fila][columna])

#Suma la primera Columna.
def columnas(matriz, largof, largoc, fila, columna, suma):
    if (fila == largof):
        return suma
    else:
        return columnas(matriz, largof, largoc, fila + 1, columna, suma + matriz[fila][columna])

#Suma antidiagonal de matriz.
def antidiagonal(matriz, largo, fila, suma):
    if (fila == largo):
        return suma
    else:
        return antidiagonal(matriz, largo, fila + 1, suma + matriz[fila][-(fila + 1)])
