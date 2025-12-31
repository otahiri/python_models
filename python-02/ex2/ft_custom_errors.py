class GardenError(Exception):
    def __init__(self, message):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message):
        super().__init__(message)


def main():
    print("=== Custom Garden Errors Demo ===")
    try:
        print("\nTesting PlantError...")
        raise PlantError("Caught PlantError: The tomato plant is wilting!")
    except PlantError as p:
        print(p)
    try:
        print("\nTesting WaterError...")
        raise WaterError("Caught WaterError: Not enough water in the tank!")
    except WaterError as w:
        print(w)
    print("\nTesting catching all garden errors...")
    try:
        raise PlantError("Caught a garden error: The tomato plant is wilting!")
    except PlantError as p:
        print(p)
    try:
        raise WaterError("Caught WaterError: Not enough water in the tank!")
    except WaterError as w:
        print(w)
    print("\nAll custom error types work correctly!")


main()
