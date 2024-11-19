"""
Una función lambda es una pequeña función anónima.
Una función lambda puede tomar cualquier número de argumentos, pero solo puede tener una expresión.
Sintaxis => lambda arguments : expression
"""

# Agregue 10 al argumento ay devuelva el resultado
x = lambda a : a + 10
print(x(5))

print("")

# Multiplica un argumento a por otro b y devuelve el resultado
x = lambda a, b : a * b
print(x(5, 6))

print("")

# Resume el argumento a, b, y c y devuelve el resultado
x = lambda a, b, c : a + b + c
print(x(11, 12, 13))

print("")

"""
El poder de lambda se muestra mejor cuando se utiliza como una función anónima dentro de otra función.
"""

# Tienes una definición de función que toma un argumento y ese argumento se multiplicará por un número desconocido
# Utilice esa definición de función para crear una función que siempre duplique el número que envíe

def mifunc(n):
  return lambda a : a * n
doble = mifunc(2)
print(doble(11))

# Utilice la misma definición de función para crear una función que siempre triplique el número que envíe
triple = mifunc(3)
print(triple(11))

"""
Utilice funciones lambda cuando se requiera una función anónima durante un corto período de tiempo
"""