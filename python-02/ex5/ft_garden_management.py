from typing import final


class PlantError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class WaterError(Exception):
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
            if not plant.name or plant.name.strip() == "":
                raise PlantError("Error adding plant: Plant name cannot be \
empty!")
            garden.crops.append(plant)
            print(f"Added {plant.name} successfully")
        except PlantError as pe:
            print(pe)
        finally:
            return

    @staticmethod
    def water_plants(garden: Garden, water: int):
        try:
            if water < 0:
                raise WaterError("Water error: negative water is invalid\
 thus rejected")
            for plant in garden.crops:
                if plant and (plant.name or plant.name.strip() != ""):
                    plant.water += water
                    print("Watering tomato - success")
                else:
                    raise PlantError("Error in plant: trying the water an \
invalid plant")
        except PlantError as pe:
            print(pe)
        except WaterError as we:
            print(we)
        finally:
            print("Closing watering system (cleanup)")

    @staticmethod
    def check_plant_health(garden: Garden):
        for plant in garden.crops:
            try:
                if plant.water < 1:
                    raise WaterError(f"Error checking {plant.name}: Water\
 level {plant.water} is too little (max 10)")
                elif plant.water > 10:
                    raise WaterError(f"Error checking {plant.name}: Water\
 level {plant.water} is too high (max 10)")
                else:
                    print(f"{plant.name}: healthy (water: {plant.water}, sun: \
{plant.sun})")
            except WaterError as we:
                print(we)


def test_garden_management() -> None:
    alice = Garden("alice")
    tomato = Plant("Tomato", 7, 5)
    lettuce = Plant("Lettuce", 14, 7)
    invalid = Plant("", 15, 7)
    print("=== Garden Management System ===")
    print("\nAdding plants to garden...")
    GardenManager.add_plant(alice, tomato)
    GardenManager.add_plant(alice, lettuce)
    GardenManager.add_plant(alice, invalid)
    print("\nWatering plants...\nOpening watering system")
    GardenManager.water_plants(alice, 1)
    print("\nChecking plant health...")
    GardenManager.check_plant_health(alice)


if __name__ == "__main__":
    test_garden_management()
