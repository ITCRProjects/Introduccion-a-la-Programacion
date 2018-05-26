#Autor: Ricardo Artavia Solano
#Entrada: Una matriz nxm y otra matriz mxr
#Salidas: El producto de las matrices de entrada resultando en una matriz nxr
#Restricciones: Las matriz 2 debe tener la misma cantidad de filas que la cantidad de columnas de la matriz 1


#Función que llama a la función principal y le pasa los parámetros
def productoMatrices(matrizA,matrizB):
    return producto(matrizA,matrizB,0,0,0,0,[])

#Función que recorre las matrices y agrega los resultados a la matriz de salida
def producto(matrizA,matrizB,indice1,indice2,indice3,operacion,nuevaMatriz):
    if len(matrizA) == indice1:
        return nuevaMatriz

    elif len(matrizB) == indice2 and len(matrizB[0])-1 == indice3:
        return producto(matrizA,matrizB,indice1+1,0,0,0,nuevaMatriz + [[operacion]])

    elif len(matrizB) == indice2:
        return producto(matrizA,matrizB,indice1,0,indice3+1,0,nuevaMatriz + [[operacion]])

    else:
        return producto(matrizA,matrizB,indice1,indice2+1,indice3,
                        operacion + calculo(matrizA,matrizB,indice1,indice2,indice3,operacion),
                        nuevaMatriz)


#Función que realiza el cálculo de los elementos por agregar al resultado
def calculo(matrizA,matrizB,indice1,indice2,indice3,operacion):
    return matrizA[indice1][indice2]*matrizB[indice2][indice3]
