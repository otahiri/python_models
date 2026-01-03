class PlantError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class Plant:
    def __init__(self, name: str, water: int, sun: int) -> None:
        self.name = name
        self.water = water
        self.sun = sun


class Garden:
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.crops = []


class GardenManager:
    @staticmethod
    def add_plant(garden: Garden, plant: Plant):
        try:
            garden.crops.append(plant)
        except PlantError as pe:
            print(pe)



alice = Garden("alice")
tomato = Plant("Tomato", 10, 5)
