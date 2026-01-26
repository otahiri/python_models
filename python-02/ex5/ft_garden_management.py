class GardenError(Exception):
    """
    garden error raise if there is an error in the garden
    """
    def __init__(self, message: str) -> None:
        """
        initialize the object garden error

        :param message: the message to display if the error is printed
        """
        super().__init__(message)


class PlantError(Exception):
    """
    plant error raise if an error occured in a plant
    """
    def __init__(self, message: str) -> None:
        """
        initialize the object plant error

        :param message: the message to display if the error is printed
        """
        super().__init__(message)


class WaterError(Exception):
    """
    water error raise if an error occured in water level
    """
    def __init__(self, message: str) -> None:
        """
        initialize the object water error

        :param message: the message to display if the error is printed
        """
        super().__init__(message)


class Plant:
    """
    the plant class has name water level and sun level
    """
    def __init__(self, name: str, water: int, sun: int) -> None:
        """
        construct the object plant

        :param name: the name of the plant
        :param water: the starting water of the plant
        :param sun: the starting value of sun exposure
        """
        if name.__class__.__name__ != "str"\
            or water.__class__.__name__ != "int"\
                or sun.__class__.__name__ != "int":
            return None
        self.name = name
        self.water = water
        self.sun = sun


class Garden:
    """
    garden class it has owner and tank attributes
    """
    def __init__(self, owner: str, tank: int) -> None:
        """
        construct the object garden

        :param owner: the name of the garden owner
        :param tank: the water level in the garden
        """
        self.tank = tank
        self.owner = owner
        self.crops = []


class GardenManager:
    """
    the manager of all gardens
    """
    @staticmethod
    def add_plant(garden: Garden, plant: Plant) -> None:
        """
        add a plant to a garden

        :param garden: the specified garden
        :param plant: the plant to add to the garden
        :raises PlantError: raise this error if the plant is invalid
                            i.e a plant with an empty plant or a None
        """
        if garden.__class__.__name__ != "Garden"\
                or plant.__class__.__name__ != "Plant":
            return None
        try:
            if not plant.name or plant.name.strip() == "":
                raise PlantError("Error adding plant: Plant name cannot be \
empty!")
            garden.crops.append(plant)
            print(f"Added {plant.name} successfully")
        except PlantError as pe:
            print(pe)

    @staticmethod
    def water_plants(garden: Garden, water: int) -> None:
        """
        water the crops in garden

        :param garden: the garden with crops
        :param water: the water level to add to each plant
        :raises WaterError: raise this error when trying to add an invalid
                            water level
        :raises PlantError: raise this error if trying to water an invalid
                            plant
        """
        if garden.__class__.__name__ != "Garden"\
                or water.__class__.__name__ != "int":
            return None
        try:
            if water < 0:
                raise WaterError("Water error: negative water is invalid\
 thus rejected")
            for plant in garden.crops:
                if plant and (plant.name or plant.name.strip() != ""):
                    plant.water += water
                    garden.tank -= water
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
    def check_plant_health(garden: Garden) -> None:
        """
        check for the health of the plants in garden

        :param garden: the garden to check the plant
        :raises WaterError: raise this error if the water is above or below
                            the specified levels
        """
        if garden.__class__.__name__ != "Garden":
            return None
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

    @staticmethod
    def check_garden_recovery(garden: Garden) -> None:
        """
        check for water in garden tank

        param garden: the garden to check
        :raises GardenError: the error to notify if the tank is empty
        """
        if garden.__class__.__name__ != "Garden":
            return None
        try:
            if garden.tank <= 0:
                garden.tank += 10
                raise GardenError("Caught GardenError: Not enough water \
in tank")
            else:
                print("the garden has enough water everything is good")
        except GardenError as ge:
            print(ge)
        finally:
            print("System recovered and continuing...")


def test_garden_management() -> None:
    """
    function to test errors in garden
    """
    alice = Garden("alice", 10)
    tomato = Plant("Tomato", 0, 8)
    lettuce = Plant("Lettuce", 10, 7)
    invalid = Plant("", 15, 7)
    print("=== Garden Management System ===")
    print("\nAdding plants to garden...")
    GardenManager.add_plant(alice, tomato)
    GardenManager.add_plant(alice, lettuce)
    GardenManager.add_plant(alice, invalid)
    print("\nWatering plants...\nOpening watering system")
    GardenManager.water_plants(alice, 5)
    print("\nChecking plant health...")
    GardenManager.check_plant_health(alice)
    print("\nTesting error recovery...")
    GardenManager.check_garden_recovery(alice)
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
