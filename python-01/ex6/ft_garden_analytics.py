class GardenManager:
    class Garden:
        crops = []
        score = 0
        garden_stats = {
            "regular": 0,
            "flowering": 0,
            "prize flower": 0
        }
        total_growth = 0

        def __init__(self, owner: str):
            self.owner = owner

    @staticmethod
    def add_crop(garden: Garden, plant):
        garden.crops.append(plant)
        if plant.__class__.__name__ == "Plant":
            garden.garden_stats["regular"] =\
                garden.garden_stats.get("regular", 0) + 1
        elif plant.__class__.__name__ == "Flower":
            garden.garden_stats["flowring"] =\
                garden.garden_stats.get("flowring", 0) + 1
        if plant.__class__.__name__ == "PrizedFlower":
            garden.garden_stats["prize flower"] =\
                garden.garden_stats.get("prize flower", 0) + 1

    @staticmethod
    def plant_care(garden: Garden, growth: int):
        garden.total_growth += growth
        print(f"\n{garden.owner} is helping all plants grow...")
        for plant in garden.crops:
            plant.height += growth
            print(f"{plant.name} grew {growth}cm")

    @staticmethod
    def print_info(garden: Garden):
        print("\n=== Alice's Garden Report ===\nPlants in garden:")
        for plant in garden.crops:
            plant.get_info()

    @staticmethod
    def print_stats(garden: Garden):
        stats = []
        for key in garden.garden_stats:
            count = garden.garden_stats[key]
            if count > 0:
                stats.append(f"{count} {key}")
        print("Plant types: ", " ".join(stats))

    @staticmethod
    def height_validation(garden: Garden):
        print(f"height_validation : \
{not any(plant.height < 0 for plant in garden.crops)}")

    @staticmethod
    def total_score(gardens):
        for garden in gardens:
            garden.score += sum(garden.height for garden in garden.crops.height)
            garden.score += len(garden.crops) * 10
            garden.score += sum(point for point in garden.crops.points)
        scores = " ".join([f"{garden.owner}: {garden.score}" for garden in gardens])
        print(f"Garden scores - {scores}")


class Plant:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def get_info(self):
        print(f"- {self.name}: {self.height}cm")

    def added_msg(self):
        print(f"Added {self.name} to Alice's garden")


class Flower(Plant):
    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)
        self.color = color

    def get_info(self):
        print(f"- {self.name}: {self.height}cm, {self.color} flowers \
(blooming)")


class PrizedFlower(Flower):
    def __init__(self, name: str, height: int, color: str,
                 points: int):
        super().__init__(name, height, color)
        self.points = points

    def get_info(self):
        print(f"- {self.name}: {self.height}cm, {self.color} flowers \
(blooming), Prize points: {self.points}")


def main():
    gardens = []
    print("=== Garden Management System Demo ===\n")
    gardens.append(GardenManager.Garden("Alice"))
    oak = Plant("Oak Tree", 100)
    GardenManager.add_crop(gardens[0], oak)
    oak.added_msg()
    rose = Flower("Rose", 25, "red")
    GardenManager.add_crop(gardens[0], rose)
    rose.added_msg()
    sunflower = PrizedFlower("Sunflower", 50, "yellow", 10)
    GardenManager.add_crop(gardens[0], sunflower)
    sunflower.added_msg()
    GardenManager.plant_care(gardens[0], 1)
    GardenManager.print_info(gardens[0])
    print(f"Plants added: {len(gardens[0].crops)}, Total growth: \
{len(gardens[0].crops) * gardens[0].total_growth}cm")
    GardenManager.print_stats(gardens[0])
    GardenManager.height_validation(gardens[0])
    GardenManager.total_score(gardens)



main()
