class GardenManager:
    """
    a main class that has inner class called Garden
    add_crop: add crops to the desired garden
    plant_care: grows plants in the desired garden
    print_info: print info about the desired garden
    print_stats: print stats about the garden such as total growth and
    number of each type of plant
    height_validation: check if any plant in a garden is invalid (negative)
    total_score: count the score of each garden managed by the class
    get_total_garden: countthe number of gardens managed by the class
    """

    class Garden:
        """
        the garden class that store the crops and info about the garden
        like the owner the total score for the garden how many of each
        plants there is and other stuff
        """

        def __init__(self, owner: str):
            """
            initialize the class Garden
            """
            self.owner = owner
            self.__score = 0
            self.crops = []
            self.garden_stats = {
                "regular": 0,
                "flowering": 0,
                "prize flower": 0
            }
            self.total_growth = 0

        def set_score(self, score: int):
            """
            set the score for the garden
            """
            self.__score = score

        def get_score(self):
            """
            return the garden score
            """
            return self.__score

    @staticmethod
    def add_crop(garden, plant):
        """
        add a plant to the desired garden
        garden: the desired garden
        plant: the plant you wanna add
        """
        garden.crops.append(plant)
        if plant.__class__.__name__ == "Plant":
            garden.garden_stats["regular"] =\
                garden.garden_stats.get("regular", 0) + 1
        elif plant.__class__.__name__ == "Flower":
            garden.garden_stats["flowring"] =\
                garden.garden_stats.get("flowring", 0) + 1
        if plant.__class__.__name__ == "PrizedFlower":
            garden.garden_stats["prize flowers"] =\
                garden.garden_stats.get("prize flower", 0) + 1

    @staticmethod
    def plant_care(garden: Garden, growth: int):
        """
        grow all plant in the desired garden by growth
        garden: the desired garden
        growth: the desired growth
        """
        garden.total_growth += growth
        print(f"\n{garden.owner} is helping all plants grow...")
        for plant in garden.crops:
            plant.height += growth
            print(f"{plant.name} grew {growth}cm")

    @staticmethod
    def print_info(garden):
        """
        print info of all plant inside the desired garden
        garden: the desired garden
        """
        print("\n=== Alice's Garden Report ===\nPlants in garden:")
        for plant in garden.crops:
            plant.get_info()

    @staticmethod
    def print_stats(garden):
        """
        print stats of the desired garden such as
        total  growth and the number of each type of plants
        garden: the desired garden
        """
        stats = []
        print(f"\nPlants added: {len(garden.crops)}, Total growth: \
{len(garden.crops) * garden.total_growth}cm")
        for key in garden.garden_stats:
            count = garden.garden_stats[key]
            if count > 0:
                stats.append(f"{count} {key}")
        print("Plant types: ", " ".join(stats))

    @staticmethod
    def height_validation(garden: Garden):
        """
        check if the height the plants inside the desired garden are valid
        garden: the desired garden
        """
        print(f"\nheight_validation : \
{not any(plant.height < 0 for plant in garden.crops)}")

    @staticmethod
    def total_score(gardens):
        """
        count the total score of all gardens managed by GardenManager
        gardens: all gardens managed by GardenManager
        """
        scores = []
        for g in gardens:
            score = g.get_score()
            g.set_score(score + sum(p.height for p in g.crops))
            g.set_score(g.get_score() + (len(g.crops) * 10))
            score = g.get_score()
            g.set_score(score + (sum(
                p.points for p in g.crops if isinstance(p, PrizedFlower))))
            score = g.get_score()
            scores.append(f"{g.owner}: {score}")
        print(f"Garden scores - {', '.join(scores)}")

    @staticmethod
    def get_total_garden(gardens):
        """
        print the total numbers of gardens managed by GardenManager
        """
        print(f"Total gardens managed: {len(gardens)}")


class Plant:
    """
    plant class a main class that represent a default class
    as in has no special features
    name: the name of the plant
    height: the height of the plant
    """
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def get_info(self):
        """
        get info about the plant such as name and height
        """
        print(f"- {self.name}: {self.height}cm")

    def added_msg(self, garden):
        """
        print the added msg to add plant to decided garden desired
        """
        print(f"Added {self.name} to {garden.owner}'s garden")


class Flower(Plant):
    """
    subclass of the Plant class same the super except it has color
    """
    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)
        self.color = color

    def get_info(self):
        """
        same as the super get_info but it prints color of the plant
        """
        print(f"- {self.name}: {self.height}cm, {self.color} flowers \
(blooming)")


class PrizedFlower(Flower):
    """
    subclass of FLower but has points trait
    """
    def __init__(self, name: str, height: int, color: str,
                 points: int):
        super().__init__(name, height, color)
        self.points = points

    def get_info(self):
        """
        same as the super get_info but prints Prize points
        """
        print(f"- {self.name}: {self.height}cm, {self.color} flowers \
(blooming), Prize points: {self.points}")


def main():
    """
        the main function that do the whole thing
    """
    gardens = []
    print("=== Garden Management System Demo ===\n")
    gardens.append(GardenManager.Garden("Alice"))
    gardens.append(GardenManager.Garden("Bob"))
    oak = Plant("Oak Tree", 100)
    GardenManager.add_crop(gardens[0], oak)
    oak.added_msg(gardens[0])
    rose = Flower("Rose", 25, "red")
    GardenManager.add_crop(gardens[0], rose)
    rose.added_msg(gardens[0])
    sunflower = PrizedFlower("Sunflower", 50, "yellow", 10)
    GardenManager.add_crop(gardens[0], sunflower)
    sunflower.added_msg(gardens[0])
    birch = Plant("Birch Tree", 82)
    GardenManager.add_crop(gardens[1], birch)
    GardenManager.plant_care(gardens[0], 1)
    GardenManager.print_info(gardens[0])
    GardenManager.print_stats(gardens[0])
    GardenManager.height_validation(gardens[0])
    GardenManager.total_score(gardens)
    GardenManager.get_total_garden(gardens)


main()
