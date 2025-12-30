class Plant:
    """
    class Plant that has age height and name
    """
    def __init__(self, name: str, height: int, ages: int):
        self.name = name
        self.height = height
        self.ages = ages

    def grow(self, days: int):
        """
        function to stimulate height increase in days given
        days: the time in days
        """
        self.height += days

    def age(self, days: int):
        """
        simulate the age increase in days given
        days: the time in days
        """
        self.ages += days

    def get_info(self, time) -> None:
        """
        get the info about the plant
        time: current time in days
        """
        print(f"=== Day {time}, ===")
        print(f"{self.name}: {self.height}cm, {self.ages} days old")


rose = Plant("Rose", 25, 30)
rose.get_info(rose.ages)
rose.age(6)
rose.grow(6)
rose.get_info(7)
print("Growth this week: +6cm")
