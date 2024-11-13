# Indicar si el elemento asignado existe en la lista
lista = ["apple", "banana", "cherry"]
if "apple" in lista:
  print("Si, 'apple' si esta en la lista")

print("")

# Cambiar valores de una lista
lista1 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
lista1[1:3] = ["blackcurrant", "watermelon"] # recordar que el valor 1 esta incluido y el valor 3 no por eso se cambia el valor 2 de la lista
print(lista1)

# La longitud de la lista cambiará cuando la cantidad de elementos insertados no coincida con la cantidad de elementos reemplazados.

print("")

# Inserta un elemento en la lista sin sustituir el otro elemento de dicha posicion
lista2 = ["apple", "banana", "cherry"]
lista2.insert(2, "watermelon")
print(lista2)

print("")

# Agregar un elemento a la lista con append()
lista3 = ["apple", "banana", "cherry"]
lista3.append("orange")
print(lista3)

print("")

# Agregar elementos de otra lista a la lista con extend()
lista4 = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
lista4.extend(tropical)
print(lista4)

print(" ")

# Eliminar un elemento de la lista con remove()
list1 = ["apple", "banana", "cherry", "banana", "kiwi"]
list1.remove("banana") # recuerda que solo eliminara la primera que encuentre
print(list1)

print("")

# Elimina un elemento especifico con pop() y del 
list2 = ["apple", "banana", "cherry"]
list2.pop(1) # si no especificas la posicion pop() eliminara el ultimo elemento
print(list2)

list3 = ["apple", "banana", "cherry"]
del list3[0]
print(list3)

print("")

# Tambien puede eliminar la lista completa 
list4 = ["apple", "banana", "cherry"]
del list4

print("")

# Dejar vacia la lista con clear()
lis1 = ["apple", "banana", "cherry"]
lis1.clear()
print(lis1)

