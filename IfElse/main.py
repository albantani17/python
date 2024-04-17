#Equals: a == b
#Not Equals: a != b
#Less than: a < b
#Less than or equal to: a <= b
#Greater than: a > b
#Greater than or equal to: a >= b

#if
a = 33
b = 200
if b > a:
  print("b is greater than a")

#Indentation
#Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.

#If statement, without indentation (will raise an error):

#Elif
print("==========")
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#Else
print("==========")
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#One Line
print("==========")
if a > b: print("a is greater than b")

#Short Hand If... Else
print("==========")
a = 2
b = 330
print("A") if a > b else "B"

print("==========")
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#And
print("==========")
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#OR
print("==========")
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#Not
print("==========")
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

#Nested If
print("==========")
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#The Pass Statement
print("==========")
a = 33
b = 200

if b > a:
  pass