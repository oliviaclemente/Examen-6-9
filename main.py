#ejercicio 6: Realiza una función separar(lista) que toma una lista de números enteros y devuelve dos listas ordenadas. la primera con los números pares y la segunda con los números impares.
def pares_impares(lista):
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
pares, impares = pares_impares(lista)
print('Pares: ', pares)
print('Impares: ', impares)
print("")
#ejercicio 7: Realizar una función llamada agregar_una_vez(lista, el) que reciba una lista y un elemento. La función debe añadir el elemento al final de la lista con la condición de no repetir ningún elemento. Además, si este elemento ya se encuentra en la lista se debe invocar un error de tipo ValueError que debes capturar y mostrar este mensaje en su lugar:Error: Imposible añadir elementos duplicados => [elemento].Cuando tengas la función intenta añadir los siguientes valores a la lista 10, -2, “Hola” y luego muestre su contenido.
Elementos = [1, 5, -2]



