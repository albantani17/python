#Remove Item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "color": "red",
  "price": "$2500"
}
thisdict.pop("model")
print(thisdict)

#Popitem()
thisdict.popitem()
print(thisdict)

#Del
del thisdict["brand"]

#CLear
thisdict.clear()
print(thisdict)
