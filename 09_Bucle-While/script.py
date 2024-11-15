# Con el bucle while podemos ejecutar un conjunto de sentencias siempre que una condición sea verdadera.
i = 1
while i <= 7:
    print(i)
    i +=1 

print("")

# Termina el blucle while con la expresion break
b = 1
while b <= 7:
    print(b)
    break
    b +=1 

print("")

# Detiene y continua con la siguiente iteracion si esta es verdadera con la expresion continue
f = 0
while f < 6:
  f += 1
  if f == 3:
    continue
  print(f)

print("")

#
l = 1
while l <= 7:
    print(l)
    l +=1
else:
   print("El numero ya pasa el limite que es '7'")
