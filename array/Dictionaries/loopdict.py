#Loop Dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():#values or keys method
    print(x)

print("==========")
for i in thisdict:
    print(thisdict[i])

print("==========")
for y in thisdict.keys():
    print(y)

print("==========")
for x, y in thisdict.items():
    print(x, y)


