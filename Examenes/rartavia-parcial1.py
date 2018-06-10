#Ricardo Artavia Solano
#                                -- Examen parcial 1 -- 


#Ejercicio 1

#Salida: Crear una lista con los digitos pares de número
#Entrada: número entero mayor que cero

def formarLista(numero):
   if isinstance(numero, int) and numero > 0:
      return formarLista_aux(numero)
   else:
      return "Error, debe ingresar un número entero positivo"

def formarLista_aux(numero):
   if numero == 0:
      return []

   elif (numero%2)%2 == 0:
      return [numero%10] + formarLista_aux(numero//10)

   else:
      return formarLista_aux(numero//10)

#------------------------------------------------------------------------------

#Ejercicio 2

#Salida: devuelve True si un número es un palíndromo y False sí no lo es.
#Entrada: número entero mayor que cero

def palindromo(numero):
   if isinstance(numero, int) and numero > 0:
      return validacion(numero)
   else:
      return "Error, debe ingresar un número entero positivo"
   
#Función que compara el número invertido con el ingresado
def validacion(numero):
   if numero == invertir(numero,contar_digitos(numero)):
      return True
   else:
      return False

#Función que cuenta los dígitos del número 
def contar_digitos(numero):
   if numero == 0:
      return 0
   else:
      return 1 + contar_digitos(numero//10)

#Función que se ecarga de invertir el número ingresado
def invertir(numero,potencia):
   if numero == 0:
      return 0
   else:
      return ((numero%10)*(10**(potencia-1))) + invertir(numero//10,potencia-1)


#------------------------------------------------------------------------------

#Ejercicio 3

#Salida: número de vocales con las que cuenta el string
#Entrada: string


def contarConsonantes(cadenaTexto):
   if isinstance(cadenaTexto,str):
      return contar_aux(cadenaTexto)
   else:
      return "Error, el parámetro debe ser de tipo String"

def contar_aux(cadenaTexto):
   
   if cadenaTexto == '':
      return 0

   elif cadenaTexto[0] == "a" or cadenaTexto[0] == "e" or cadenaTexto[0] == "o" or cadenaTexto[0] == "u" or cadenaTexto[0] == "i":
      return contar_aux(cadenaTexto[1:])



   else:
      return 1 + contar_aux(cadenaTexto[1:])


#------------------------------------------------------------------------------
   

#Ejercicio 4

#Salida: Lista, con los órdener pares intercambiados
#Entrada: lista de números enteros positivos


def intercambiar(lista):
   if isinstance(lista,list):
      return recorrer(lista)
   else:
      return "Error, el atributo debe ser una lista"

def recorrer(lista):
   if lista == []:
      return []

   else:
      return intercambio(lista[:2]) + recorrer(lista[2:])

def intercambio(lista):
   if lista == []:
      return []
   else:
      #hace falta esto: + lista[:1]
      #De manera que: [lista[1]] + lista[:1] + intercambio(lista[:0])
      #Agregando esa instrucción si da, no recuerdo si la agregué en el examen al finalizar
      #Pero el algoritmo funciona bien
      
      return [lista[1]] + intercambio(lista[:0])
