#ejercicio 1: Al realizar una consulta en un registro hemos obtenido una cadena de texto corrupta al revés. Al parecer contiene el nombre de un alumno y la nota de un exámen. ¿Cómo podríamos formatear la cadena y conseguir una estructura como la siguiente?Nombre Apellido ha sacado un Nota de nota.AyudaPara voltear una cadena rápidamente utilizando slicing podemos utilizar un tercer índice -1: cadena[::-1], 
print("ejercicio 1")
cadena = "zeréP nauJ,01"
l= cadena[::-1].split(",")
print(l[1] + " ha sacado un "+ l[0] +" de nota")
print("")

#ejercicio3:Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, pero no debe repetirse ningún elemento en la nueva lista:
print("ejercicio3")
lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
lista_3=[]
for letra in lista_1:
  if letra in lista_2 and letra not in lista_3:
    lista_3.append(letra)
print(lista_3)
print("")

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

#ejercicio 7: Realizar una función llamada agregar_una_vez(lista, el) que reciba una lista y un elemento. La función debe añadir el elemento al final de la lista con la condición de no repetir ningún elemento. Además, si este elemento ya se encuentra en la lista se debe invocar un error de tipo ValueError que debes capturar y mostrar este mensaje en su lugar:Error: Imposible añadir elementos duplicados => [elemento].Cuando tengas la función intenta añadir los siguientes valores a la lista 10, -2, “Hola” y luego muestre su contenido.
print("ejercicio 7")
elementos = [1, 5, -2]
def agregar_una_vez(elemento):
  if elemento in elementos:
    print(f"Error al añadir elementos duplicados => {elemento}")
  else: 
    elementos.append(elemento)
    
agregar_una_vez(1)
print(elementos)
print("")

#ejercicio8: Utilizando todo lo que sabes sobre cadenas, listas, sus métodos internos… Transforma este texto: Un día el viento soplaba con fuerza#mira cómo se mueve aquella banderola-dijo un monje#lo que se mueve es el viento -respondió otromonje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes – dijo el maestro En este otro: Un día que el viento soplaba con fuerza… - Mira cómo se mueve aquella banderola – dijo un monje. - Lo que se mueve es el viento – respondió otro monje. - Ni las banderolas ni el viento, lo que se mueve son vuestras mentes – dijo el maestro. Lo único prohibido es modificar directamente el texto.
print("ejercicio8")
texto= "Un día el viento soplaba con fuerza#mira cómo se mueve aquella banderola-dijo un monje#lo que se mueve es el viento -respondió otromonje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes – dijo el maestro"
lineas = texto.split("#")
for i, linea in enumerate(lineas):
    lineas[i]= linea.capitalize()
    if i == 0:
      lineas[i] = lineas[i] + "..."
    else: 
      lineas[i] = "-" + lineas[i] + "."
for linea in lineas:
  print(linea)
print("")