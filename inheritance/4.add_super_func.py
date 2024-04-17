class Parent:
    def __init__(self,fname,lname) -> None:
        self.fname = fname
        self.lname = lname
    
    def display(self):
        print(self.fname, self.lname)

class Child(Parent):
    def __init__(self, fname, lname) -> None:
        super().__init__(fname, lname)

x = Child("John", "Doe")
x.display()

#By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.