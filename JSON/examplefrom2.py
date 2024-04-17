# Example
# Convert a Python object containing all the legal data types:

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# print(json.dumps(x))

#Indent spasi untuk X

#Separators untuk merubah default separator

# print(json.dumps(x, indent=1, separators=(".","=")))

#Order the Result
#Mengurutkan array dari abjad A-Z
print(json.dumps(x, indent=5, sort_keys=True))