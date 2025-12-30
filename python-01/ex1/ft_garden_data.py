class Plant:
    """
    plant class the has 3 attributes
    name: the name of the plant
    height: the height of the plant
    age: the age of the plant
    """
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


rose = Plant("Rose", 25, 30)
sunflower = Plant("Sunflower", 80, 45)
cactus = Plant("Cactus", 15, 120)
print("=== Garden Plant Registry ===")
print(rose.name, ":", rose.age, "Days", rose.height, "cm")
print(sunflower.name, ":", rose.age, "Days", rose.height, "cm")
print(cactus.name, ":", rose.age, "Days", rose.height, "cm")
