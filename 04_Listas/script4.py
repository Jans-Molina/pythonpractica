# copia una lista con el metodo list()
milista = ["apple", "banana", "cherry"]
nuevalista = list(milista)
print(nuevalista)

print("")

# Concatenar 2 listas 
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

"""
append()	Agrega un elemento al final de la lista
clear()	    Elimina todos los elementos de la lista
copy()	    Devuelve una copia de la lista
count()	    Devuelve el número de elementos con el valor especificado
extend()	Agrega los elementos de una lista (o cualquier iterable), al final de la lista actual
index()	    Devuelve el índice del primer elemento con el valor especificado
insert()	Agrega un elemento en la posición especificada
pop()	    Elimina el elemento en la posición especificada
remove()	Elimina el elemento con el valor especificado
reverse()	Invierte el orden de la lista
sort()	    Ordena la lista
"""