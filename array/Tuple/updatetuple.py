#Change Tuple Values
print("=========")
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(f"List 1 = {x}")

#Add Itemms
#1
print("=========")
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print(thistuple)

#2
print("=========")
y = ("orange",)
thistuple += y

print(thistuple)

#Remove Items

print("=========")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

print(f"list remove = {thistuple}")

#delete whole tuple
del thistuple
print(thistuple)
