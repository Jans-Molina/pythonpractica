# Las funciones puede devolver un valor booleano
def myFunction() :
  return True

print(myFunction())

# Un ejemplo con if
def myFunction1() :
  return 0

if myFunction1():
  print("YES!")
else:
  print("NO!")

# Comprueba si un valor es entero o no con isinstance()
x = 200
print(isinstance(x, str))