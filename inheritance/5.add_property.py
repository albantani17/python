#Add Properties
class Parent:
    def __init__(self,fname,lname) -> None:
        self.fname = fname
        self.lname = lname
    
    def display(self):
        print(self.fname, self.lname)

class Child(Parent):
    def __init__(self, fname, lname) -> None:
        super().__init__(fname, lname)
        self.age = 19

x = Child("Alban", "Haerul")    
print(x.age)

#Contoh lain
class Kid(Parent):
    def __init__(self, fname, lname, year) -> None:
        super().__init__(fname, lname)
        self.age = year

x = Kid("Mike","gtw",5)
x.display()
print(x.age)