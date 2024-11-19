"""
Una función es un bloque de código que solo se ejecuta cuando se lo llama.
"""
# Crea una Funcion con el metodo def

def mifuncion():
    print("Hola, Como estas?")
mifuncion()

print("")

# Agrega mas argumentos cuando llamas a la funcion
def mifuncion1(fname):
  print(fname + " Cortes")
mifuncion1("Emilia")
mifuncion1("Tobias")
mifuncion1("Linux")

"""
Desde la perspectiva de una función:
Un parámetro es la variable que aparece dentro de los paréntesis en la definición de la función.
Un argumento es el valor que se envía a la función cuando se llama.
"""

print("")

# Crea una funcion que espere 2 argumentos
def misfunciones(faname, laname):
  print(faname + " " + laname)
misfunciones("Emil", "Refsnes") # Si le envias 1 o 3 argumentos esta imprimira un error por que esta esperando 2 argumentos 

print("")

# Si se desconoce el número de argumentos agregue un * antes del nombre del parámetro
def mifuncion2(*niños):
  print("El niño mas pequeño es " + niños[2])
mifuncion2("Emilia", "Tobias", "Linux")

print("")

# Envia argumentos con clave = valor, de esta manera el orden de los argumentos no importa
def mifuncion3(niño3, niño2, niño1):
  print("El niño mas joven es " + niño3)
mifuncion3(niño1 = "Vale", niño2 = "Tom", niño3 = "Lin")

print("")

# Si no sabe cuántos argumentos de palabras clave se pasarán a su función, agregue dos asteriscos: ** antes del nombre del parámetro en la definición de la función
# De esta manera, la función recibirá un diccionario de argumentos y podrá acceder a los elementos en consecuencia
def mifuncion4(**niño):
  print("Su apellido es " + niño["apellido"])
mifuncion4(nombre = "Tobias", apellido = "Molina")

print("")

# El siguiente ejemplo muestra cómo utilizar un valor de parámetro predeterminado. Si llamamos a la función sin argumentos, utiliza el valor predeterminado:
def mifun(pais = "Norway"):
  print("Yo soy de " + pais)

mifun("Sweden")
mifun("India")
mifun()
mifun("Brazil")

print("")

"""
Puede enviar cualquier tipo de datos de argumento a una función (cadena, número, lista, diccionario, etc.) 
y se tratará como el mismo tipo de datos dentro de la función.
Por ejemplo, si envía una lista como argumento, seguirá siendo una lista cuando llegue a la función:
"""
def mifun1(comida):
  for x in comida:
    print(x)
frutas = ["apple", "banana", "cherry"]
mifun1(frutas)

print("")

# Para permitir que una función devuelva un valor, utilice la return declaración
def mifuncion5(x):
  return 5 * x
print(mifuncion5(3))
print(mifuncion5(5))
print(mifuncion5(9))

print("") 

"""
Las definiciones no pueden estar vacías, pero si por alguna razón tienes una function definición
sin contenido, ponla en la pass declaración para evitar obtener un error.

def myfunction():
  pass
"""