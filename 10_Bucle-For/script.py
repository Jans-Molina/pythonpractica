"""
EL BUCLE for SOLO SIRVE PARA ITERAR CON SECUENCIAS COMO STR, LIST, TUPLA, DICCIONARIO Y SET) 
"""

# Muestra los elementos de una lista con el bucle for
milista = ["Hola", "Como", "Estas", "?"]
for x in milista:
    print(x)

print(milista[1]) # Para mostrar un solo elemento indexeado

print("")

# Recorreo el contenido de un str con for

for x in "abcdef":
    print(x)

print("")

# Detiene el bucle con un break
frutas = ["Manzana", "Platano", "Pera", "Uva"]
for x in frutas:
    print(x)
    if x == "Pera": # Si quieres que no se imprima la condicion tiene que poner el print() despues del salto
        break

print("")

# con la expresion continue poder detener el bucle y continuara con la siguiente.
for x in frutas:
  if x == "Platano":
    continue
  print(x)

print("")

# Crea un rango de numeros especificos para las vueltas del bucle con el metodo range() (el ultimo numero especificado no esta incluido)
for x in range(1,6): #al especificar un 3er numero este contara como saltos entre ellos range(1,10,2)
  print(x)

print("")

# Imprime una frase al final un bucle con else
for x in range(6):
  print(x)
else:
  print("Final!")

print("")

# Bucles anidados es un bucle dentro de un bucle con for se ejecutara el bucle principal una vez por cada iteracion con el bucle externo 
adj = ["Maduro", "Verde", "Podrido"]
for x in adj:
   for y in frutas:
      print(x, y)

"""
for Los bucles no pueden estar vacíos, pero si por alguna razón tienes un for bucle sin contenido, ponlo en la
pass declaración para evitar obtener un error.

for x in [0, 1, 2]:
  pass
"""