class Plant:
    """
    class Plant
    attributes:
    name: the name of the plant
    height: the height of the plant in cm
    ages: the age of the plant in days
    """
    count = 0

    def __init__(self, name: str, height: int, ages: int):
        """
        a contructor

        name: the name of the plant
        height: the height of the plant cm
        ages: the age of the plant in days
        """
        Plant.count += 1
        self.name = name if name else "Unknown"
        self.height = height if height else 0
        self.ages = ages if ages else 0

    def grow(self, days: int):
        """
        function to stimulate height increase in days given
        days: age in days
        """
        self.height += days

    def age(self, days: int):
        """
        simulate the age increase in days given
        days: age in days
        """
        self.ages += days

    def get_creation_info(self):
        """
        print info about the creation of the plant
        """
        print(f"Created: {self.name} ({self.height}cm, {self.ages} days)")


print("=== Plant Factory Output ===")
crops = {
    1: ["Rose", 25, 30],
    2: ["Oak", 200, 365],
    3: ["Cactus", 5, 90],
    4: ["Sunflower", 80, 45],
    5: ["Fern", 15, 120]
}
for key in crops:
    name, height, age = crops[key]
    plant = Plant(name, height, age)
    plant.get_creation_info()
print(f"\nTotal plants created: {Plant.count}")
