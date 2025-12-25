class Plant:
    """
        class Plant that has age height and name
    """
    def __init__(self, name: str, height: int, ages: int):
        """
            class constructor to make the class object
        """
        self.name = name
        self.height = height
        self.ages = ages

    def grow(self, days: int):
        """
            function to stimulate height increase in days given
        """
        self.height += days

    def age(self, days: int):
        """
            simulate the age increase in days given
        """
        self.ages += days

    def get_info(self, time) -> None:
        """
            get the info about the plant
        """
        print("=== Day", time, "===")
        print(f"{self.name}: {self.height}cm, {self.ages} days old")


rose = Plant("Rose", 25, 30)
rose.get_info(1)
rose.age(6)
rose.grow(6)
rose.get_info(7)
print("Growth this week: +6cm")
