class GardenManager:
    class Garden:
        crops = []

        def __init__(self, owner: str):
            self.owner = owner

        def add_crop(self, plant):
            self.crops.append(plant)


class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        print(f"- {self.name}: {self.height}cm")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int):
        super().__init__(name, height, age)

    def get_info(self):
        print(f"- {self.name} {self.__class__.__name__}: {self.height}cm")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color


class Prized(Flower):
    def __init__(self, name: str, height: int, age: int, color: str,
                 points: int):
        super().__init__(name, height, age, color)
        self.points = points


def main():
    alice_garden = GardenManager.Garden("Alice")
    alice_garden.add_crop(Plant(""))
