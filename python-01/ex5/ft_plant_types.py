import math


class Plant:
    def __init__(self, name: str, age: int, height: int):
        self.name = name
        self.__age = 0
        self.__height = 0
        self.set_height(height)
        self.set_age(age)

    def set_age(self, age: int):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_height(self, height: int):
        self.__height = height

    def get_height(self):
        return self.__height


class Flower(Plant):
    def __init__(self, name: str, color: str, age: int, height: int):
        super().__init__(name, age, height)
        self.color = color

    def get_info(self):
        print(f"\n{self.name} ({__class__.__name__}): {self.get_height()}cm,  \
days, {self.color} color")
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, diameter: int, age: int, height: int):
        super().__init__(name, age, height)
        self.diameter = diameter

    def get_info(self):
        print(f"\n{self.name} ({__class__.__name__}): {self.get_height()}cm, \
{self.get_age()} days, {self.diameter} diameter")
        num = int(self.get_height()) // 100
        print(f"Oak provides {int(math.pi * (num**2))} square \
meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, h_time: str, vi: str, age: int, height: int):
        super().__init__(name, age, height)
        self.harvest_time = h_time
        self.vitamin = vi

    def get_info(self):
        print(f"\n{self.name} ({__class__.__name__}): {self.get_height()}cm, \
{self.get_age()} days, {self.harvest_time} harvest")
        print(f"{self.name} is rich in vitamin {self.vitamin}")


print("=== Garden Plant Types ===")
rose = Flower("Rose", "Red", 30, 25)
rose.get_info()
oak = Tree("Oak", 50, 1825, 500)
oak.get_info()
tomato = Vegetable("Tomato", "summer", "C", 90, 80)
tomato.get_info()
