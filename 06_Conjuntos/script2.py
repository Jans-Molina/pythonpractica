# Unir 2 conjuntos diferentes
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
# Tambien se pueden unir usando el simbolo |
set4 = {"a", "b", "c"}
set5 = {1, 2, 3}
set6 = set4 | set5
print(set6)

print("")

# union() tambien sirve para unir varios conjuntos mas (y tambien usando el simbolo | como el ejemplo anterior)
set7 = {"a", "b", "c"}
set8 = {1, 2, 3}
set9 = {"John", "Elena"}
set10 = {"apple", "bananas", "cherry"}
myset1 = set7.union(set8, set9, set10)
print(myset1)

"""
El simbolo | solo permite unir conjuntos con conjuntos, y no con otros tipos de datos como puede hacerlo con el union().
"""

print("")

# Tambien puedes unir conjuntos con el metodo update()
set11 = {"a", "b" , "c"}
set12 = {1, 2, 3}
set11.update(set12)
print(set11)

print("")

# Devuelve en un nuevo conjunto todos los elementos que esten multiplicados en ambos conjuntos con el metodo intersection()
set13 = {"apple", "banana", "cherry"}
set14 = {"google", "microsoft", "apple"}
set15 = set13.intersection(set14)
print(set15)

# Utiliza el simbolo & para mostrar elementos multiplicados de los conjuntos a unir (Solo entre conjuntos)

"""
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)
"""
print("")

# Interseccion_update() realizara lo casi lo mismo solo que en vez de crear un conjunto nuevo, este lo reemplaza en el original

set16 = {"apple", "banana", "cherry"}
set17 = {"google", "microsoft", "apple"}
set16.intersection_update(set17)
print(set16)

print("")

# Devuelve todos los elementos que no esten presenten en el otro conjunto con el metodo difference()
set18 = {"apple", "banana", "cherry"}
set19 = {"google", "microsoft", "apple"}
set20 = set18.difference(set19)
print(set20)

# Utilizando el simbolo - tendremos el mismo resultado anterior (Esto metodo es solo entre conjuntos)
"""
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)
"""

# Tambien obtener los elementos con difference_update() en el conjunto original
set21 = {"apple", "banana", "cherry"}
set23 = {"google", "microsoft", "apple"}
set21.difference_update(set23)
print(set21)

print("")

# Mostrar los elementos que no esten en ambos conjuntos con el metodo symmetric_difference()
set24 = {"apple", "banana", "cherry"}
set25 = {"google", "microsoft", "apple"}
set26 = set24.symmetric_difference(set25)
print(set26)

# Con el simbolo ^ obtienes lo mismos resultados anterior (Solo es entre conjuntos con este metodo)
"""
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)
"""
