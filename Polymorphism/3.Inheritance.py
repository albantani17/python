class Device:
    def __init__(self,brand,model) -> None:
        self.brand = brand
        self.model = model

    def move(self):
        print("TouchScreen")

class Handphone(Device):
    pass

class Laptop(Device):
    def move(self):
        print("Cursor")

class Console(Device):
    def move(self):
        print("Controller")

hp = Handphone("Xiaomi", "redmi note 8")
laptop = Laptop("Asus", "vivobook")
konsol = Console("Nintendo","Switch")

for x in (hp,laptop,konsol):
    print(x.brand)
    print(x.model)
    x.move()