fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(
car.get("model")
)
car["year"]= 2020
print(car.get("year")) 

car["color"]="red"
print(car.get("color"))

car.pop("model")
print(car.get("model"))