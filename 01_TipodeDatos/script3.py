x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

print(" ")

q = r = p = "Orange"
print(q)
print(r)
print(p)

print(" ")

fruits = ["apple", "banana", "cherry"]
xx, yy, zz = fruits
print(xx)
print(yy)
print(zz)

print(" ")

x1 = "awesome"

def myfunc():
  x1 = "fantastic"
  print("Python is " + x1)

myfunc()

print("Python is " + x1)

print(" ")

def myfunc():
  global x2
  x2 = "fantastic"

myfunc()

print("Python is " + x2)