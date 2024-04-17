#add items
print("=========")
thisset = {"a","b","c"}
thisset.add("g")
print(thisset)

#add from another sets
print("=========")
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#add any iterable
print("=========")
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)