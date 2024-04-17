print("=========")

#Access tuple items
tuple1 = ("apple", "banana", "cherry")
print(tuple1[1]) 
print("=========")
#negativ index
print(tuple1[-1]) 

print("=========")
#Range of index
tuple2 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tuple2[2:5])
print("=========")
print(tuple2[:4])

print("=========")
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

#Range of negative index
print("=========")
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#check  if item is in the tuple
print("=========")
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")