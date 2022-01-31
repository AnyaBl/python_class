import math
a = float(input("Enter parameter  a : "))
b = float(input("Enter parameter b : "))
c = float(input("Enter parameter c : "))

discr = b**2 - 4 * a * c

if discr > 0:
  x1 = (-b + math.sqrt(discr)) / (2 * a)
  x2 = (-b - math.sqrt(discr)) / (2 * a)
  print("x1 = ", x1, "x2=",  x2)
elif discr == 0:
  x0 = -b / (2 * a)
  print("x=", x0)
else:
  print("There are no roots of the equation")