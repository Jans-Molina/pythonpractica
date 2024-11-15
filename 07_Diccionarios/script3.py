# Recorre los elementos del diccionario imprimiendo la clave
midiccionario =	{
  "Marca": "Ford",
  "Modelo": "Mustang",
  "Año": 1964
}
for x in midiccionario:
  print(x)

print("")

# Imprimir los valores de los elementos del diccionario
for x in midiccionario:
  print(midiccionario[x])

print("")

# Imprimir los valores de un diccionario con values()
for x in midiccionario.values():
  print(x)

print("")

# Imprimir las claves de un diccionario con keys()
for x in midiccionario.keys():
  print(x)

print("")

# Imprimir las claves junto con los valores con items()
for x, y in midiccionario.items():
  print(x, y)

print("")

# Copiar un diccionario existente en uno nuevo con el metodo copy()
nuevodiccionario = midiccionario.copy()
print(nuevodiccionario)

# Copiar un diccionario existente en uno nuevo con el metodo dict()
nuevodiccionario1 = dict(midiccionario)
print(nuevodiccionario1)

print("")

# Crea un diccionario que contenga diccionarios (Esto se le llama diccionarios anidados)
mifamilia = {
  "persona1" : {
    "nombre" : "Emil",
    "año" : 2004
  },
  "persona2" : {
    "nombre" : "Tobias",
    "año" : 2007
  },
  "persona3" : {
    "nombre" : "Linus",
    "año" : 2011
  }
}

print(mifamilia)

print("")

# Para acceder a los elementos de un diccionario anidado, comienza con el nombre del diccionario y despues su clave
print(mifamilia["persona2"]["nombre"])


# Recorre diccionarios anidados con el metodo item()
for x, obj in mifamilia.items():
    print("")
    print(x)
    
    for y in obj:
        print(y + ':', obj[y])

print("")
