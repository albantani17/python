#Remove spesifik item
thislist1 = ["apple", "banana", "cherry"]
thislist1.remove("banana")
print(f"list 1 {thislist1}")

#Remove spesifik index
thislist2 = ["apple", "banana", "cherry"]
thislist2.pop(0)
print(f"list 2 {thislist2}")

thislist3 = ["apple", "banana", "cherry"]
thislist3.pop()
print(f"list 2 {thislist3}")

thislist4 = ["apple", "banana", "cherry"]
del thislist4[2]
print(f"list 2 {thislist4}")

thislist5 = ["apple", "banana", "cherry"]
thislist5.clear()
print(f"list 5 {thislist5}")