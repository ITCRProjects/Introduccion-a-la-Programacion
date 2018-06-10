class Producto:
    def __init__(self,matrizA,matrizB):
        self.indice1 = 0
        self.indice2 = 0
        self.indice3 = 0
        self.operacion = 0
        self.nuevaMatriz = []
        self.matrizA = matrizA
        self.matrizB = matrizB

    def producto(self,matrizA,matrizB,indice1,indice2,indice3,operacion,nuevaMatriz):
        if len(self.matrizA) == self.indice1:
            return self.nuevaMatriz

        elif len(self.matrizB) == self.indice2 and len(self.matrizB[0]) - 1 == self.indice3:
            return producto(self, matrizA, matrizB, indice1 + 1, 0, 0, 0, nuevaMatriz + [[operacion]])

        elif len(self.matrizB) == self.indice2:
            return producto(self,matrizA, matrizB, indice1, 0, indice3 + 1, 0, nuevaMatriz + [[operacion]])

        else:
            return producto(self, matrizA, matrizB, indice1, indice2 + 1, indice3, operacion + matrizA[indice1][indice2]*matrizB[indice2][indice3],nuevaMatriz)

