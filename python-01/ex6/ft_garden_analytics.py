class Plant:
    def __init__(self, name: str, height: int, state: str):
        self.name = name
        self.__height = height
        self.state = state

    def set_height(self, height: int):
        if height > 0:
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")
        else:
            print(f"\nInvalid operation attempted: height {height}cm \
[REJECTED]")
            print("Security: Negative height rejected\n")

    def grow(self, growth: int):
        self.set_height(self.get_height() + growth)

    def get_height(self):
        return self.__height

    def get_info(self):
        print(f"- {self.name}: {self.get_height()}cm)")


class Flower(Plant):
    def __init__(self, name: str, height: int, color: str, state: str):
        super().__init__(name, height, state)
        self.color = color

    def get_info(self):
        print(f"- {self.name}: {self.get_height()}cm, {self.color} flowers \
(blooming)")


class PrizedFlower(Flower):
    def __init__(self, name: str, height: int, points: int,
                 color: str, state: str):
        super().__init__(name, height, color, state)
        self.prize_points = points

    def get_info(self):
        print(f"- {self.name}: {self.get_height()}cm, {self.color} flowers\
 (blooming), Prize points: {self.prize_points}")


class Tree(Plant):
    def __init__(self, name: str, height: int, state: str):
        super().__init__(name, height, state)

    def get_info(self):
        print(f"- {self.name} {self.__class__.__name__}: {self.get_height()}\
cm")


class Garden:
    plant_count = 0
    total_growth = 0
    total_regular = 0
    total_flowering = 0
    total_prized_flowers = 0

    def __init__(self, owner: str) -> None:
        self.garden = [None]
        self.owner = owner
        self.crops = []

    def add_crop(self, crop: Plant):
        self.crops.append(crop)
        self.plant_count += 1
        print(f"Added {crop.name} to {self.owner}'s\
 garden")
        self.total_regular += crop.state == "regular"
        self.total_flowering += crop.state == "flowering"
        self.total_prized_flowers += crop.state == "prize flowers"

    def garden_care(self, growth: int):
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.crops:
            plant.grow(growth)
            self.total_growth += growth

    def get_garden_info(self):
        print("=== Alice's Garden Report ===\nPlants in garden:")
        for plant in self.crops:
            plant.get_info()
        print(f"Plants added: {self.plant_count}, Total growth: \
{self.total_growth}cm")
        print(f"Plant types: {self.total_regular} regular, \
{self.total_flowering} flowering, {self.total_prized_flowers} prize flowers")


def main():
    print("=== Garden Management System Demo ===\n\n")
    alice_garden = Garden("Alice")
    alice_garden.add_crop(Tree("Oak", 100, "regular"))
    alice_garden.add_crop(Flower("Rose", 25, "Red", "flowering"))
    alice_garden.add_crop(PrizedFlower("Sunflower", 50, 10, "yollow",
                                       "prize flowers"))
    print("")
    alice_garden.garden_care(1)
    alice_garden.get_garden_info()


main()
