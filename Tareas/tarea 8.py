class Tarea9:

    def __init__(self):
        pass

    def binaria(self,lista,elemento):
        self.lista = lista
        self.elemento = elemento
        self.inicio = 0
        self.final = len(self.lista)-1
        self.mitad = (self.inicio + self.final)//2

        for i in self.lista:
            if self.elemento != self.lista[self.mitad]:
                
                if self.elemento < self.lista[self.mitad]:
                    self.inicio = self.inicio
                    self.mitad = (self.inicio + self.final)//2
                    self.final = self.mitad-1

                elif self.elemento > self.lista[self.mitad]:
                    self.inicio = self.mitad + 1
                    self.mitad = (self.inicio + self.final) // 2
                    self.final = self.final

        print("Siendo 0 la primer posición, el número se encuentra en la posición: ", self.mitad)



