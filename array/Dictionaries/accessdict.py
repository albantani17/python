#access items
dict1 = {
 "brand": "Ford",
  "model": "Mustang",
  "year": 1964   
}
x = dict1["model"]

print("==========")
print(x)

j = dict1.keys()
print("==========")
print(j)

dict1 ["color"] = "white"
print(j)

#Get Values

print("==========")
y = dict1.values()
print(y)

#Get Items
z=dict1.items()
print("========")
print(z)

#Check  if a Key exists in the Dictionary
print("========")
if "brand" in dict1:
    print("Yes, model in here")