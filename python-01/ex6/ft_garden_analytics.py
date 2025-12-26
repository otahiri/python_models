class Plant:
    count = 0
    valid_height = True

    @classmethod
    def increase_count(cls):
        cls.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

    def __init__(self, name: str, height: int, state: str):
        self.name = name
        self.__height = height
        self.state = state

    def set_height(self, height: int):
        if height > 0:
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")
        else:
            self.valid_height = False
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
    flowering = 0

    def __init__(self, name: str, height: int, color: str, state: str):
        super().__init__(name, height, state)
        self.flowering += 10
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
    total_growth = 0
    total_regular = 0
    total_flowering = 0
    total_prized_flowers = 0

    def __init__(self, owner: str) -> None:
        self.garden = [None]
        self.owner = owner
        self.crops = []


class GardenManager:

    growth = 0

    def __init__(self, garden):
        self.garden = garden

    class GardenStats:
        @staticmethod
        def total_height(Plants):
            return sum(p.get_height() for p in Plants)

    def garden_care(self, growth: int):
        print(f"{self.garden.owner} is helping all plants grow...")
        self.growth += growth
        for plant in self.garden.crops:
            plant.grow(growth)
            self.garden.total_growth += growth

    def add_crop(self, crop: Plant):
        self.garden.crops.append(crop)
        Plant.increase_count()
        print(f"Added {crop.name} to {self.garden.owner}'s\
 self.garden")
        self.garden.total_regular += crop.state == "regular"
        self.garden.total_flowering += crop.state == "flowering"
        self.garden.total_prized_flowers += crop.state == "prize flowers"

    def get_score(self):
        return self.garden.GardenStats.total_height(self.garden.crops)\
            + (self.garden.prize_points * 10)\
            + (self.garden.total_flowering * 10)

    def get_garden_info(self):
        print("=== Alice's Garden Report ===\nPlants in garden:")
        for plant in self.garden.crops:
            plant.get_info()
        print(f"Plants added: {Plant.count}, Total growth: \
{Plant.count * self.growth}cm")
        print(f"Plant types: {self.garden.total_regular} regular, \
{self.garden.total_flowering} flowering, \
{self.garden.total_prized_flowers} prize flowers")

    def garden_total_score(self):
        print(f"Height validation test: {Plant.valid_height}")
        print(f"Garden scores - Alice: {self.get_score()}, Bob: 92")


def main():
    print("=== Garden Management System Demo ===\n\n")
    alice_garden = Garden("Alice")
    garden_manager = GardenManager(alice_garden)

    garden_manager.add_crop(Tree("Oak", 100, "regular"))
    garden_manager.add_crop(Flower("Rose", 25, "Red", "flowering"))
    garden_manager.add_crop(PrizedFlower("Sunflower", 50, 10, "yollow",
                                         "prize flowers"))
    garden_manager.garden_care(1)
    garden_manager.get_garden_info()
    garden_manager.garden_total_score()

main()
