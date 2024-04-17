#Join Two Lists
print("=========")
list1 = ["a","b","c"]
list2 = [1,2,3]
#Using the "+" operator to join two
result = list1 + list2
print(f"List 1 + 2 = {result}")  #Output: ['a', 'b', 'c', 1, 2, 3]

#atau bisa menggunakan append
print("=========")
for x in list2:
    list1.append(x)

print(f'List append = {list1}')

#Bisa juga menggunakan extend()
print("=========")

list1.extend(list2)
print(f"List extend = {list1}")   #Output: ['a', 'b', 'c', 1, 2,  3]