# Para especificar que una función solo puede tener argumentos posicionales agregue , / después de los argumentos
def mifuncion(x, /):
  print(x)
mifuncion(3)

# Se permite usar argumentos de palabras clave incluso si la función espera argumentos posicionales
def mifuncion1(x):
  print(x)
mifuncion1(x = 3)
"""
Pero al agregarlo, , / obtendrá un error si intenta enviar un argumento de palabra clave

def my_function(x, /):
  print(x)
my_function(x = 3)
"""
print("")

# Especifica que una función solo puede tener argumentos de palabras clave, agregue *, antes de los argumentos
def mifuncion2(*, x):
  print(x)
mifuncion2(x = 3)

"""
Sin él * se permite utilizar argumentos posicionales incluso si la función espera argumentos de palabras clave

def my_function(x):
  print(x)
my_function(3)

Pero * obtendrás un error si intentas enviar un argumento posicional

def my_function(*, x):
  print(x)
my_function(3)
"""

print("")

# Puede combinar los dos tipos de argumentos en la misma función.
# Cualquier argumento antes de / ,son solo posicionales, y cualquier argumento después de *, son solo palabras clave

def mifuncion3(a, b, /, *, c, d):
  print(a + b + c + d)
mifuncion3(5, 6, c = 7, d = 8)

print("")

# ESTUDIAR A FONDO LO QUE ES RECURSION EN PYTHON/ MODULO FUNCIONES