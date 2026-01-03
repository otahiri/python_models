class Plant:
    """
    plant class
    attributes:
    name: string that holds the name of the plant
    height: an integer that hold the plant height in cm
    age: an integer that hold the age of the plan in days
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        a constructor
        name: the name of the plant
        height: the height of the plant in cm
        age: the age of the plant in days
        """
        self.name = name
        self.height = height
        self.age = age


rose = Plant("Rose", 25, 30)
sunflower = Plant("Sunflower", 80, 45)
cactus = Plant("Cactus", 15, 120)
print("=== Garden Plant Registry ===")
print(f"{rose.name}: {rose.height}cm, {rose.age} days old")
print(f"{sunflower.name}: {sunflower.height}cm, {sunflower.age} days old")
print(f"{cactus.name}: {cactus.height}cm, {cactus.age} days old")
