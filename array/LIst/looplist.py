#Loop Through a List
thislist1 = ["apple", 1, True]
for x in thislist1:
    print(f"list 1 {x}")

print("=========")

#Loop Through the Index Number
thislist2 = ["apple", 1, True]
for i in range(len(thislist2)):
    print(f"list 2 {i}")

print("=========")

#Using a While Loop
thislist3 = ["apple", 1, True]
i = 0
while i < len(thislist3):
    print(f"List 3 {thislist3[i]}")
    i = i + 1

print("=========")

#Looping Using List Comprehenshiom
thislist4 = ["apple", 1, True]
[print(x) for x in thislist4]