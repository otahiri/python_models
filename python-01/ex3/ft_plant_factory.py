class Plant:
    """
    class Plant that has age height and name
    """
    count = 0

    def __init__(self, name: str, height: int, ages: int):
        Plant.count += 1
        self.name = name
        self.height = height
        self.ages = ages
        self.get_creation_info()

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

    def get_info(self):
        """
        get the info about the plant
        """
        print(f"{self.name}: {self.height}cm, {self.ages} days old")

    def get_creation_info(self):
        print(f"Created: {self.name} ({self.height}cm, {self.ages} days)")


print("=== Plant Factory Output ===")
rose = Plant("Rose", 25, 30),
oak = Plant("Oak", 200, 365),
cactus = Plant("Cactus", 5, 90),
sunflowe = Plant("Sunflower", 80, 45),
fern = Plant("Fern", 15, 120),
print("\nTotal plants created:", Plant.count)
