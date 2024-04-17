class Binatang:
    def bersuara(self):
        pass

class Kucing(Binatang):
    def bersuara(self):
        return "meow"
    
class Anjing(Binatang):
    def bersuara(self):
        return "ANJING"
    
def suara_hewan(hewan):
    return hewan.bersuara()

anjing = Anjing()
kucing = Kucing()

print(suara_hewan(anjing))
print(suara_hewan(kucing))


#Contoh lain

class Bike:
    def __init__(self, brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("GAsss")

class Car:
    def __init__(self, brand,model) -> None:
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Drive")

class Plane:
    def __init__(self,brand,model) -> None:
        self.brand = brand
        self.model = model
        pass

    def move(self):
        print("fly")

car = Car("Ferrary","F1")
bike = Bike("ltb","12")
plane = Plane("Garuda","X55")

for x in (car,bike,plane):
    print(x.model)
    print(x.brand)
    x.move()