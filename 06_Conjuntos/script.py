# Crear un conjunto
set1 = {"apple", "banana", "cherry"}
print(set1)

print("")

# No permite elementos multiplicados
set2 = {"apple", "banana", "cherry", "apple"} 
print(set2)

"""
true y 1 seran conciderados datos iguales.
y
false y 0 seran conciderados de igual manera.
"""

print("")

# Saber cuantos elementos tiene un conjunto
set3 = {"apple", "banana", "cherry", "juanito"}
print(len(set3))

print("")

# Pueden contener cualquier tipo de datos en los conjuntos
"""
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {"abc", 34, True, 40, "male"}
"""

# Crear un conjunto con el constructor set()
set4 = set(("apple", "banana", "cherry"))
print(set4)

print("")

# No se puede acceder a los elementos de un conjunto haciendo referencia a un índice o una clave.
# Recorreo los elementos del conjunto con for()
set5 = {"apple", "banana", "cherry", "pencil", "car", "buggy"}
for x in set5:
  print(x)

print("")

# Busca un elemento especifico de un conjunto (y para saber si este no esta presente se agrega el not antes del in)
set6 = {"apple", "banana", "cherry"}
print("banana" in set6)

print("")

# Agregar elementos nuevos a un conjunto con add()
set7 = {"apple", "banana", "cherry"}
set7.add("orange")
print(set7)

print("")

# Agregar otra lista puede ser cualquiera de las 4 tipos en este caso una lista con update()
set8 = {"apple", "banana", "cherry"}
list1 = ["kiwi", "orange"]
set8.update(list1)
print(set8)

print("")

# Elimina un elemento especifico de un conjunto con discard() ya que este no genera un error al momento de no encontrar el elemento.
# remove() genera un error al no encontrar el elemento.
set9 = {"apple", "banana", "cherry"}
set9.discard("banana")
print(set9)

print("")

# El metodo pop() elimina un elemento aleatorio debido a que el conjunto no esta indexeado
set10 = {"apple", "banana", "cherry"}
x1 = set10.pop()
print(x1) 
print(set10) 

print("")

# Vaciar un conjunto borrando todos sus elementos con clear()
set11 = {"apple", "banana", "cherry"}
set11.clear()
print(set11)

print("")

# Elimina el conjunto con el metodo del()
set12 = {"apple", "banana", "cherry"}
del set12
print(set12) # Imprimira un error debido a que ya no existira el conjunto
