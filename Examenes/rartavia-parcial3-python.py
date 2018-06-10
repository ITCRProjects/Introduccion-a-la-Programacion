class Parte1:
	def __init__(self,numero):
		#Como optimización se puede pasar la variable numero como argumento del metodo contar
		self.numero = numero
		self.contador = 0
		self.contador2 = 0

	#Ejercicios de la Parte 1
	#Este método indica cuantos digitos posee un número
	def contar(self):
		while self.numero//10 != 0:
			self.numero = self.numero//10
			self.contador = self.contador + 1
		print("El número ingresado tiene: ")
		print(self.contador+1)


	#Este método ordena una lista de números
	def ordenarLista(self,lista):
		self.lista = lista
		while self.contador2 <= len(self.lista):
			for i in range(0,len(self.lista)-1):
				if self.lista[i] < self.lista[i+1]:
					self.lista[i] = self.lista[i+1]
					self.lista[i+1] = self.lista[i]
				self.contador2 = self.contador2 + 1
		print("El resultado de ordenar la lista es: ", self.lista)

	#Inicio de ejercicio de la Parte 2
	#Método que realiza la multilpicación de matrices
	def multiplicacion(self,matrizA,matrizB):
		self.matrizC = [[]]
		self.contadorFilas = 0
		self.mB = matrizB
		self.mA = matrizA
		self.k = 0
		self.resultado = 0
		self.contador = 0

		while self.contador < ((len(self.mA)*len(self.mB[0]))+1):
			if self.k == len(self.mB[0]):
				self.contadorFilas = self.contadorFilas + 1
				self.resultado = 0
				self.k = 0

				for j in range(0,len(self.mA[0])):
					self.resultado =  self.resultado + (self.mA[self.contadorFilas][j]*self.mB[j][self.k])
					j = j +1
				j = 0
				self.k = self.k + 1
				self.matrizC = self.matrizC + [[self.resultado]]
				self.contador = self.contador + 1

			else:
				self.resultado = 0
				for j in range(0,len(self.mA[0])):
					self.resultado = self.resultado + (self.mA[self.contadorFilas][j]*self.mB[j][self.k])
					j = j+1
				j = 0
				self.k = self.k + 1
				self.matrizC = self.matrizC + [[self.resultado]]
				self.contador = self.contador + 1
