#WHile Loops
print("==========")
i = 1
while i < 6:
    print(i)
    i += 1
    
#Break Statement    
print("==========")
y = 1
while y < 10:
    print(y)
    if y == 5:
        break
    y += 1

#Continue Statement
print("==========")
x = 1
while  x < 10:
    x += 1
    if x == 3:
        continue
    print(x)

#Else Statement
print("==========")
num = 1
while num < 5:
    print(num)
    num += 1
else:
    print("number is no longer than 5")
