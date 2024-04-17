#Copy Lists
print("=========")

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()  # Creates a new list that is identical
print(f"List 1 = {mylist}")

print("=========")

mylist1 = list(thislist)
print(f"List 2 = {mylist1}")