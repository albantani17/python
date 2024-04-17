class Parent:
    def __init__(self,fname,lname) -> None:
        self.fname = fname
        self.lname = lname
    
    def display(self):
        print(self.fname, self.lname)

class Child(Parent):
    def __init__(self, fname, lname, year) -> None:
        super().__init__(fname, lname)
        self.year = year

    def welcome(self):
        print(f"Happy birthday {self.fname} {self.lname} now your age is {self.year}")

x =  Child("John", "Doe", 2)
x.welcome()