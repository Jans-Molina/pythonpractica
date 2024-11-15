# Una declaracion simple utilizando if con una condicion
a = 101
b= 100
if a > b:
    print("A es mayor que B")

print("")

# elif() sirve cuando la condicion de if no es correcta, agrega una nueva condicion
c = 100
d = 100
if c > d:
    print("C es mayor que D")
elif c == d:
    print("C es igual que D") 

print("")

# else() si es que no se cumplen las condiciones anteriores se ejecuta.
e = 200
f = 33
if f > e:
  print("f es mayor que e")
elif e == f:
  print("e y f son iguales")
else:
  print("e es mayor que f")

print("")

print("")

# Tambien solo puedes tener un else()

z = 200
y = 33
if y > z:
  print("y es mayor que z")
else:
  print("y no es mayor que z")

print("")

# and sirve para agregar mas condiciones a la declaracion 
aa = 200
bb = 33
cc = 500
if aa > bb and cc > aa:
  print("Ambas condiciones son verdaderas")

print("")

# or sirve para imprimir cualquiera de las 2 condiciones que se especifique si es que una de las 2 no se cumple.
t = 200
u = 33
p = 500
if t > u or t > p:
  print("Almenos una de las condiciones es verdadera")

print("")

# Comprueba si un numero no es mayor que el otro con not
a1 = 33
b1 = 200
if not a1 > b1:
  print("a no es mayor que b")

print("")

"""
Puedes terner if dentro de un if, esto se le llama declaracion anidadas

x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
"""

"""
ifLas declaraciones no pueden estar vacías, pero si por alguna razón tiene una if declaración
sin contenido, coloque la passdeclaración para evitar obtener un error.

a = 3
b = 2

if a < b:
    pass
"""