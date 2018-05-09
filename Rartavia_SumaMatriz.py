

#Ricardo Artavia Solano
#Entradas: Matriz
#Salidas: La suma de todos los elementos y el valor promedio de los mismos
def suma_matriz(matriz):
    if isinstance(matriz,list):
        return matriz_aux(matriz,0,0,len(matriz[0]),len(matriz),0)
    else: return "Error"

def matriz_aux(matriz,num_fila,num_columna,columnas,filas,suma):
    if num_fila == filas:
        print("La matriz contiene el siguiente numero de elementos:",suma)
        print("El valor promedio de los elementos es:", suma/(columnas*filas))

    elif num_columna == columnas:
        return matriz_aux(matriz,num_fila + 1,0,columnas,filas,suma)

    else:
        return matriz_aux(matriz,num_fila,num_columna + 1,columnas,filas,suma + (matriz[num_fila][num_columna]))
