mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))

print(mylist)

def my_function(x):
  return list(dict.fromkeys(x))

mylist = my_function(["a", "b", "a", "c", "c"])

print(mylist)