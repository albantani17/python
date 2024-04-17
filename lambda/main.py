#syntax

print("==========")

x = lambda a : a + 10
print(x(5))

print("==========")

y = lambda a, b : a*b
print(y(2,3))

print("==========")
z = lambda a,b,c : a + b - c
print(z(4,6,2))

print("==========")
def myfunc(n):
    return lambda a : a * n

mydouble = myfunc(3)
print(mydouble(11))

print("==========")
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
