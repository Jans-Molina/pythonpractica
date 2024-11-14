# Creacion de una tupla
tuplex = ("apple", "banana", "cherry")
print(tuplex)

print("")

# Las tuplas pueden ser cualquier tipo de datos
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("abc", 34, True, 40, "male") # tambien puede contener cualquier tipo de dato

print(tuple1)
print(tuple2)
print(tuple3)
print(tuple4)

print("")

# Crear un tuple con el constructor tuple()
tuplee = tuple(("apple", "banana", "cherry"))
print(tuplee)

print("")

# Puedes llamar un elemento especifico de la tupla
tupla1 = ("apple", "banana", "cherry")
print(tupla1[1])

print("")

# Consultar si un elemento esta presente en la tupla
tupla2 = ("apple", "banana", "cherry")
if "apple" in tupla2:
  print("Si, 'apple' se encuentra en la tupla")

print("")

# Debido a que la tupla es inmutable hay una solucion alternativa para modificarla, creandola a lista y asi viceversa a tupla
x1 = ("apple", "banana", "cherry")
y1 = list(x1)
y1[1] = "kiwi"
x1 = tuple(y1)
print(x1)

print("")

# Forma alternativa de agregar un elemento a la tupla
tuplex1 = ("apple", "banana", "cherry")
y2 = list(tuplex1)
y2.append("orange")
tuplex1 = tuple(y2)
print(tuplex1)

print("")

# Agregar una tupla a una tupla existente
tuplexx = ("apple", "banana", "cherry")
y3 = ("orange",)
tuplexx += y3
print(tuplexx)

print("")

# Eliminar un elemento especifico de una tupla de forma alternativa
thi = ("apple", "banana", "cherry")
y4 = list(thi)
y4.remove("apple")
thi = tuple(y4)
print(thi)