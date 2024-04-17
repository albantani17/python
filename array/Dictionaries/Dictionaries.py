#Dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("=========")
print(thisdict)

#Return 1 value
print("=========")
print(thisdict["model"])

#Not Allowed Duplicate
thisdict2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year":  2005 # This will overwrite the previous year key-value pair.
}
print("=========")
print(thisdict2)

#Length
print("=========")
print(len(thisdict))

#Data Types
#Str, INt, Boolean, and list data can be use
my_hp = {
  "brand" : "Redmi",
  "model" :  "Note 8 Pro",
  "year" :  2019,
  "color" : ["Black","White"]
}
print("==========")
print(my_hp)

#Type()
print("==========")
print(type(my_hp))

#The Dict() Constructor

dict1 = dict(name = "Micheal Moody", age =  37, city= "New York")
print("=======")
print(dict1)