a = input("Ingrese un numero : ")
b = input("Ingrese un numero mayor al anterior : ") 

if b > a:
  print("Ingresaste un numero mayor, correcto!")
else:
  print("Ingresaste un numero menor, error!")

print("")

"""
Casi cualquier valor se evalúa True si tiene algún tipo de contenido.
Cualquier cadena es True, excepto las cadenas vacías.
Cualquier número es True, excepto 0.
Cualquier lista, tupla, conjunto y diccionario son True, excepto los vacíos.
"""
# Los siguientes valores son falsos
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))