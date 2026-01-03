class Plant:
    """
    class Plant
    attributes:
    name: the name of the plant
    height: the height of the plant in cm
    age: the age of the plant in days
    """
    def __init__(self, name: str, height: int, ages: int):
        """
        a constructor

        name: the name of the plant
        height: the height of the plant in cm
        ages: the age of the plant
        """
        self.name = name
        self.height = height
        self.ages = ages

    def grow(self):
        """
        function to stimulate height increase in days given
        days: the time in days
        """
        self.height += 1

    def age(self):
        """
        simulate the age increase in days given
        days: the time in days
        """
        self.ages += 1

    def get_info(self, time) -> None:
        """
        get the info about the plant
        time: current time in days
        """
        print(f"=== Day {time} ===")
        print(f"{self.name}: {self.height}cm, {self.ages} days old")


count = 1
rose = Plant("Rose", 25, 30)
rose.get_info(count)
for i in [1, 2, 3, 4, 5, 6]:
    rose.age()
    rose.grow()
    count += 1
rose.get_info(count)
print("Growth this week: +6cm")
