#Create a Parent Class
class Parent:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname,self.lname)

#Use the Parent class to create an object, and then execute the printname method:
        
x = Parent("Alban", "Haerul")
x.printname()

#Create a Child Class (Inheritance) from the Parent Class
class Child(Parent):
    pass

x = Child("Sultan", "Dongo")
x.printname()
