# Obtener el valor de la clave Modelo
midiccionario =	{
  "Marca": "Ford",
  "Modelo": "Mustang",
  "Año": 1964
}
x = midiccionario["Marca"]
print(x)

# Tambien el metodo get() dara el mismo resultado anterior
x1 = midiccionario.get("Modelo")
print(x1)

print("")

# El metodo keys() devolvera una lista con todas las claves del diccionario
x2 = midiccionario.keys()
print(x2)

print("")

# El metodo values() devolvera una lista con todos los valores del diccionario
x3 = midiccionario.values()
print(x3)

print("")

# El metodo items() devolvera todo el contenido del diccionario ordenandolos en clave:valor como tupla en una lista
x4 = midiccionario.items()
print(x4)

print("")

# Comprueba si una clave especifica esta presente en un diccionario con in
if "Modelo" in midiccionario:
  print("Si, 'Modelo' es una llave del diccionario")

print("")

# Cambiar el valor de una llave especifica
midiccionario1 =	{
  "marca": "Ford",
  "modelo": "Mustang",
  "año": 1964
}
midiccionario1["año"] = 2023
print(midiccionario1)

print("")

# Actualiza tambien la clave:valor especifica con el metodo update()
midiccionario1.update({"año": 2020})
print(midiccionario1)

print("")

# Agrega una nueva llave con su valor al diccionario ya existente
midiccionario2 =	{
  "marca": "Ford",
  "modelo": "Mustang",
  "año": 1964
}
midiccionario2["color"] = "red"
print(midiccionario2)

"""
Con el metodo update() que sirve para actualizar un elemento, si es que cuyo elemento no existe este se agregara como nuevo elemento del diccionario.
"""

print("")

# Elimina un elemento con la clave del valor especifica con el metodo pop()
midiccionario3 = {
  "marca": "Ford",
  "modelo": "Mustang",
  "año": 1964
}
midiccionario3.pop("modelo")
print(midiccionario3)

"""
popitem() elimina el ultimo elemento del diccionario 
"""

print("")

# Elimina un elemento especifico del diccionario con el metodo del() (y tambien sirve para eliminar el diccionario por completo)
del midiccionario3["año"]
print(midiccionario3)