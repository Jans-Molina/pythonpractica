# Para mostrar todo los elementos de una lista con for()
lista = ["apple", "banana", "cherry"]
for x in lista:
  print(x)

print("")

# Muestra todo los elementos de una lista con while()
lista1 = ["apple", "banana", "cherry"]
i = 0
while i < len(lista1):
  print(lista1[i])
  i = i + 1

print("")

# Rescatar todos los elementos de una lista que contengan la letra "a" (sin comprension de lista)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

print("")

# Rescatar todos los elementos de una lista que contengan la letra "a" (con compresion de lista)
fruits1 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist1 = [x for x in fruits1 if "a" in x]
print(newlist1)

print("")

# Solo rescata los elementos que no se llamen apple (con compresion de lista)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist2 = [x for x in fruits if x != "apple"]
print(newlist2)

print("")

# puedes crear una lista cambiando el iterable
list1 = [x for x in range(10)]
print(list1)

list2 = [x for x in range(10) if x < 5] # con condicion
print(list2)

print("")

# Manipular la expresion para que cambien todas por "hola"
fruta = ["apple", "banana", "cherry", "kiwi", "mango"]
new = ['hello' for x in fruta]
print(new)

frui = ["apple", "banana", "cherry", "kiwi", "mango"]
newli = [x if x != "banana" else "orange" for x in frui]# con una condicion
print(newli)

print("")

# Ordenar la lista dependiendo de su valor con sort()
this = ["orange", "mango", "kiwi", "pineapple", "banana"]
this.sort() # Ordena alfabeticamente
print(this)

print("")

# Ordena la lista desde el numero menor a mayor con key =
def myfun(n):
  return abs(n - 50)

th = [100, 50, 65, 82, 23]
th.sort(key = myfun)
print(th)


