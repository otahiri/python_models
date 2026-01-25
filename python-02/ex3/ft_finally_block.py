def water_plants(plant_list: list) -> None:
    """
    waters plants

    :param plant_list: the list of diffrent plants to test this on
    :raises TypeError: raised when a plant is invalid
    """
    if plant_list.__class__.__name__ != "list":
        return
    print("Opening watering system")
    for plant in plant_list:
        if plant.__class__.__name__ != "str":
            raise TypeError("Error: Cannot water None - invalid plant!")
        print(f"Watering {plant}")


def test_watering_system() -> None:
    """
    test  watering system
    """
    print("\nTesting normal watering...")
    try:
        water_plants(["tomato", "lettuce", "carrots"])
    except TypeError as te:
        print(te)
    finally:
        print("Closing watering system (cleanup)")
    print("\nTesting with error...")
    try:
        water_plants(["tomato", [None], "lettuce", "carrots"])
    except TypeError as te:
        print(te)
    finally:
        print("Closing watering system (cleanup)")
    print("Watering completed successfully!")

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    test_watering_system()
