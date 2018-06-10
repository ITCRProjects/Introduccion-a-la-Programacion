def binaria(num, lista):
   if isinstance(num, int) and  (lista, list):
      return binaria_aux(num, lista, len(lista)//2)
   else:
      return -1

def binaria_aux(num, lista, mitad):
   if (lista == []):
      return False
   elif (num == lista[mitad]):
      return True
   elif (num > lista[mitad]):
      return binaria_aux(num, lista[(mitad+1):], mitad//2)
   elif (num < lista[mitad]):
      return binaria_aux(num, lista[:(mitad+1)], mitad//2)
