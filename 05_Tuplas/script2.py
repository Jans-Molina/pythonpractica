# Obtener los elementos de una tupla en bucle con for()
tuple = ("apple", "banana", "cherry")
for x in tuple: 
  print(x)

print("")

# Obtener los elementos de una tupla en bucle con while()
tuple2 = ("apple", "banana", "cherry")
i1 = 0
while i1 < len(tuple2):
  print(tuple2[i1])
  i1 = i1 + 1

  print("")

# Unir tuplas diferentes
tuplee1 = ("a", "b" , "c")
tuplee2 = (1, 2, 3)
tuplee3 = tuplee1 + tuplee2
print(tuplee3)

"""
count()	Devuleve el numero de veces que aparece un valor especificado en una tupla
index()	Busca en la tupla un valor específico y devuelve la posición donde se encontró
"""