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
        print(f"Created: {self.name} ({self.height}cm, {self.ages} days)")

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


print("=== Plant Factory Output ===")
rose = Plant("Rose", 25, 30)
oak = Plant("Oak", 200, 365)
cactus = Plant("Cactus", 5, 90)
sunflower = Plant("Sunflower", 80, 45)
fern = Plant("Fern", 15, 120)
print(f"\nTotal plants created: {Plant.count}")
