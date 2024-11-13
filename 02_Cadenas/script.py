# Recuerda que el 1er caracter tiene posicion [0]
a = "Hello, World!"
print(a[1])

# consigue el valor entre las posiciones asignadas
b = "Hello, World!"
print(b[2:5])

print(" ")

# Genera un bucle que recorre todo el valor
for x in "banana":
  print(x)

print(" ")

# Devuelve la longitud del valor
a2 = "Hello, World!"
print(len(a2))

print(" ")

# Comprueba si free esta en el valor de la variable
txt = "The best things in life are free!"
print("free" in txt)

# Con un if 
txt1 = "The best things in life are free!"
if "free" in txt1:
  print("Yes, 'free' is present.")

print(" ")

# Devuelve los valores en mayusculas 
a1 = "Hello, World!"
print(a1.upper())

# Devuelve los valores en minusculas
a3 = "Hello, World!"
print(a3.lower())

# Reemplaza el valor especifico por otro

aa = "Hello, World!"
print(aa.replace("H", "Hh"))