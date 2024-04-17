#For Loops
print("==========")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#Looping Through a String
print("==========")
for x in "banana":
  print(x)

#The Break Statement
print("==========")
for i in fruits:
  print(i)
  if i ==  "banana":
    break
  
print("==========")
for i in fruits:
  if i == "banana":
    break
  print(i)

#Continue Statement
print("==========")
for j in fruits:
  if j == "banana":
    continue
  print(j)

#Range Function()
print("========")
for z in range(5):
  print(z)

print("========")
for a in range(2,6):
  print(a)

print("========")
for x in range(2, 30, 3):
  print(x)

print("========")
for b in range(6):
    print(b)
else:
  print("Finally finished!")

#Else block will not be executed if the loop is stopped by break statement
print("========")
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#Nested Loops
print("========")
adj = ["red", "big", "tasty"]
fruits2 = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits2:
    print(x, y)

#Pass Statement
for x in [0,1,2]:
  pass