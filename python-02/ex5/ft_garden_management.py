class WaterError(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)


class PlantError(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)


class GardenError(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)


class Plant:
    def __init__(self, name) -> None:
        self.name = name
        self.water = 0
        self.sun = 0


class GardenManager:
    class Garden:
        def __init__(self, water_tank: int) -> None:
            self.water_tank = water_tank
            self.crops = []

    @staticmethod
    def add_plant(garden: Garden, plant: Plant):
        try:
            if plant.name:
                garden.crops.append(plant)
            else:
                raise PlantError("Error adding plant: Plant name cannot \
be empty!")
        except PlantError as pe:
            print(pe)
        finally:
            print(f"Added {plant.name} successfully")

    @staticmethod
    def water_plant(plant: Plant, water_level: int, garden: Garden):
        try:
            if (garden.water_tank - water_level) < 0:
                raise GardenError("Caught GardenError: Not enough water in \
tank")
        except GardenError as ge:
            print(ge)
        try:
            if not (1 <= water_level + plant.water <= 10):
                raise WaterError(f"Error water level {water_level + plant.water}  exceed \
the limit (max is 10 and min is 1)")
        except WaterError as we:
            print(we)
        finally:
            print(f"Watering {plant.name} - success")
            plant.water += water_level

    @staticmethod
    def check_plant_health(plant: Plant):
        try:
            if plant.water < 2:
                raise WaterError(f"Error checking {plant.name}: Water level {plant.water} is too low (min 1)")
            elif plant.water > 10:
                raise WaterError(f"Error checking {plant.name}: Water level {plant.water} is too high (max 10)")
            elif plant.sun > 12:
                raise WaterError(f"Error checking {plant.name}: Sunlight hours {plant.sun} is too long (max 12)")
            elif plant.sun < 2:
                raise WaterError(f"Error checking {plant.name}: Sunlight hours {plant.sun} is too short (min 12)")
        except WaterError as we:
            print(we)
        except PlantError as pe:
            print(pe)
        except GardenError as ge:
            print(ge)
        finally:
            print(f"{plant.name}: healthy (water: {plant.water}, sun: {plant.sun})")


def test_garden_management():
    print("Adding plants to garden...")
    garden = GardenManager.Garden(100)
    GardenManager.add_plant(garden, Plant("Tomato"))
    GardenManager.add_plant(garden, Plant("Lettuce"))
    GardenManager.add_plant(garden, Plant(None))


test_garden_management()
