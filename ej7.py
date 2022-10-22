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