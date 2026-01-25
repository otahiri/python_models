class GardenError(Exception):
    """
    garden error raised if an error occured in a garden
    """
    def __init__(self, message: str) -> None:
        """
        initalize the object garden error

        :param message: the message to display if the error is printed
        """
        super().__init__(message)


class PlantError(GardenError):
    """
    plant error raise if an error occured in a plant
    """
    def __init__(self, message: str) -> None:
        """
        initalize the object plant error

        :param message: the message to display if the error is printed
        """
        super().__init__(message)


class WaterError(GardenError):
    """
    water error raised if an error occured in water level
    """
    def __init__(self, message: str) -> None:
        """
        initalize the object water error

        :param message: the message to display if the error is printed
        """
        super().__init__(message)


def main() -> None:
    """
    the main function that tests the errors

    :raises PlantError: raise when an error occured in plant
    :raises WaterError: raised when an error occured in water level
    :raises GardenError: raised when an error occurse in the garden
    """
    try:
        print("\nTesting PlantError...")
        raise PlantError("Caught PlantError: The tomato plant is wilting!")
    except PlantError as p:
        print(p)
    try:
        print("\nTesting WaterError...")
        raise WaterError("Caught WaterError: Not enough water in the tank!")
    except GardenError as ge:
        print(ge)
    print("\nTesting catching all garden errors...")
    try:
        raise PlantError("Caught a garden error: The tomato plant is wilting!")
    except GardenError as ge:
        print(ge)
    try:
        raise WaterError("Caught WaterError: Not enough water in the tank!")
    except GardenError as ge:
        print(ge)


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    main()
    print("\nAll custom error types work correctly!")
