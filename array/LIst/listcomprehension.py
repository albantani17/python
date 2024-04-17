#List Comprehension

print("=========")

#without comprehension
fruits = ["apple", "banana", "cherry","kiwi","mango"]
newlist = []
for i in fruits:
    if "a" in i:
        newlist.append(i)

print(f"list tanpa comprehension")
print(newlist)

print("=========")

#with comprehension
newlist2 = [i for i in fruits if "a" in i]
print("Dengan comprehension")
print(newlist2)

print("=========")

#Condition
newlist3 = [i for i in fruits if i != "banana"]
print(newlist3)

print("=========")

newlist4 = [i for i in fruits]
print(len(newlist4))
print(newlist4)

print("=========")

newlist5 = [i for i in range(10)]
print(newlist5)

print("=========")

newlist6 = [x for x in range(10) if x <= 5]
print(newlist6)

print("=========")

newlist7 = [x.upper() for x in fruits]
print(newlist7)

print("=========")

newlist8 = ['hello' for x in fruits]
print(newlist8)

print("=========")

newlist9 = [x if x != "banana" else "orange" for x in fruits]
print(newlist9)