def water_plants(plant_list):
    """
    waters plants

    :param plant_list: the list of diffrent plants to test this on
    :raises TypeError: raised when a plant is invalid
    """
    print("Opening watering system")
    try:
        for plant in plant_list:
            if not isinstance(plant, str):
                raise TypeError
            print(f"Watering {plant}")
    except TypeError:
        print("Error: Cannot water None - invalid plant!")
        return
    finally:
        print("Closing watering system (cleanup)")
    print("Watering completed successfully!")


def test_watering_system():
    """
    test  watering system
    """
    print("\nTesting normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("\nTesting with error...")
    water_plants(["tomato", [None], "lettuce", "carrots"])
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    test_watering_system()
