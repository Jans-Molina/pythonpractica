# Crea un diccionario 
midiccionario = {
    "Marca": "Ford",
    "Modelo": "Mustang",
    "Año": 1964
}
print(midiccionario)

print("")

# Imprimir el valor Marca del diccionario
print(midiccionario["Marca"])

"""
Los valores duplicados sobrescribirán los valores existentes:
"""

print("")

# Imprimir los numeros de elementos que se encuentran en el diccionario 
print(len(midiccionario))

print("")

# Los valores de los elementos del diccionario pueden ser de cualquier tipo de datos (en este caso str, int, bool, list)
midiccionario1 = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(midiccionario1)

print("")

# Crear un diccionario con el constructor dict()
midiccionario2 = dict(nombre = "Jans", edad = 23, ciudad = "Canela")
print(midiccionario2)

print("")

