thislist1 = ["apple", "banana", "cherry"]
print(len(thislist1))

thislist2 = list(("apple", "banana", "cherry"))
print(thislist2)

thislist3 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist3[2:5])

#This will return the items from position 2 to 5.

#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included
thislist4 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist4[:4])

#This will return the items from index 0 to index 4.

#Remember that index 0 is the first item, and index 4 is the fifth item
#Remember that the item in index 4 is NOT included

thislist5 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist5[2:])

thislist6 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist6[-4:-1])

thislist7 = ["apple", "banana", "cherry"]
if "apple" in thislist7:
  print("Yes, 'apple' is in the fruits list")
else:
  print("Its Not Exist")