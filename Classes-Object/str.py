#The __str__() Function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass
    def __str__(self):
        return f"Namaku adalah {self.name} umurku {self.age}"

data = Person("Alban", 19)

print(data)