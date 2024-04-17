print("==========")
class Orang:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"
p = Orang("Alban", 19)
print(p)

#Modify Object Properties
print("==========")
p.age = 20
print(p)

#Delete Object Propertiess
del p.age
#print(p) #Output akan error karena objeknya sudah hilang

#The pass Statement
#class definitions cannot be empty, but if you for some reason have a class definition with no content, 
#put in the pass statement to avoid getting an error.

#Contoh
class Person:
    pass