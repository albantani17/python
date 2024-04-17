#Alphanumerically

print("=========")

thislist1 = ["apple", "banana", "cherry","kiwi","mango"]
thislist1.sort()
print(f"List 1 = {thislist1}")

print("=========")

thislist2 = [60,55, 20,22,33]
thislist2.sort()
print(f"List 2 = {thislist2}")

#Descending
print("=========")

thislist3 = ["apple", "banana", "cherry","kiwi","mango"]
thislist3.sort(reverse= True)
print(f"List 3 = {thislist3}")

print("=========")

thislist4 = [60,55, 20,22,33]
thislist4.sort(reverse=True)
print(f"List 4 = {thislist4}")

#Customize sort function

print("=========")

def myfunc(n):
    return abs(n - 50)

thislist5 = [100,20,30,45,50]
thislist5.sort(key= myfunc)
print(f"List 5 = {thislist5}")

#Case Insensitive Sort

print("=========")
#Sort by default akan mengurutkan list dari huruf kapital ke huruf kecil
thislist6 = ["banana", "Orange", "Kiwi", "cherry"]
thislist6.sort()
print(f"List 6 = {thislist6}")
#Untuk membuat case insensitive bisa menggunakan key str.lower untuk mengurutkan sesuai alphabet
print("=========")
thislist6.sort(key=str.lower) 
print(f"List 6 = {thislist6}")

#Reverse Order
print("=========")
thislist7 = ["banana", "Orange", "Kiwi", "cherry"]
thislist7.reverse()
print(f"List 7 = {thislist7}")