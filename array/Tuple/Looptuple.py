

thistuple = ("apple", "banana", "cherry")


#loop through a tuple
print("=========")
for x in thistuple:
    print(x)

#Loop through the index numbers
print("=========")
for i in range(len(thistuple)):
    print(thistuple[1])

#Using a while loop
print("=========")
i = 0
while i < len(thistuple):
    print(thistuple[1])
    i += 1