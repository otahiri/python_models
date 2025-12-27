class GardenManagerclass:
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


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color


class Prized(Flower)  g
