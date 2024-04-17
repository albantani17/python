#add items
thislist1 = ["apple", "banana", "cherry"]
thislist1.append("peach")
print(f"List 1 {thislist1}")

#Insert Items
thislist2 = ["apple","banana", "cherry"]
thislist2.insert(1, "mango")
print(f"List 2 {thislist2}")
print(len(thislist2))

#Extend list
thislist3 = ["apple","banana", "cherry"]
tropical = ["mango", "pineapple", "durian"]
thislist3.extend(tropical)
print(f"List 3 {thislist3}")

#Add Any Iterable
thislist4 = ["apple","banana", "cherry"]
thistuple = ("alban","oktober")
thislist4.extend(thistuple)
print(f"List 4 {thislist4}")