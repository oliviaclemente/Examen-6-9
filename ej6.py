#ejercicio 6: Realiza una función separar(lista) que toma una lista de números enteros y devuelve dos listas ordenadas. La primera con los números pares y la segunda con los números impares.
print("ejercicio 6")
def separar(lista):
  pares= []
  impares= []
  for i in lista:
    if i%2 == 0:
      pares.append(i)
    else: 
      impares.append(i)
  pares.sort()
  impares.sort()
  return pares, impares
  
lista = [6,5,2,1,7]
pares, impares = separar(lista)
print('Pares: ', pares)
print('Impares: ', impares)
print("")