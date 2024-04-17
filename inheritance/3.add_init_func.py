#Add init Function
class Parent:
    def __init__(self,fname,lname) -> None:
        self.fname = fname
        self.lname = lname

    def display(self):
        print(self.fname, self.lname)
        
class Student(Parent):
    def __init__(self, fname, lname):
        Parent.__init__(self,fname, lname)

x = Student("Alban", "Ganteng")
x.display()

