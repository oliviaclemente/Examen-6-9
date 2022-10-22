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