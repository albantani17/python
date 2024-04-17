#Set
print("=========")
thisset = {"apple", "banana", "cherry", "mango"}
print(thisset)

#Duplicate not allowed
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#True and 1 is the same value
print("=========")
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

#length
print("=========")
print(len(thisset))

#Set Items - Data Types
#bisa int,float, str, boolean
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#bisa dicampur juga dengan tipe data yang lain
set1 = {"abc", 34, True, 40, "male"}

#Type
print("=========")
myset = {"apple", "banana", "cherry"}
print(type(myset))

#The set
print("=========")
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)