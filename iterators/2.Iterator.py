#Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.

#All these objects have a iter() method which is used to get an iterator:

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit)) # Outputs: apple
print(next(myit)) # Outputs: banana

# for x in myit:
#     print(x)