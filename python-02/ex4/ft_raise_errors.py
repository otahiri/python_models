def check_plant_health(plant_name, water_level, sunlight_hours) -> str:
    """
    check the health of the plant

    :param plant_name: the name of the plant
    :param water_level: the water level to set of the plant
    :param sunlight_hours: the hours the sun shine on the plant
    :raises ValueError: raised when an error occures in the plant or one of
                        the parameters
    """
    if water_level.__class__.__name__ != "int"\
            or sunlight_hours.__class__.__name__ != "int"\
            or plant_name.__class__.__name__ != "str":
        raise ValueError("invalid values please enter valid values\
 a string for the plant_name and a number for water_level and sunlight_hours")
    elif not plant_name:
        raise ValueError("Error: Plant name cannot be empty!")
    elif water_level > 10:
        raise ValueError(f"Error: Water level {water_level} is too high \
(max 10)")
    elif water_level < 1:
        raise ValueError(f"Error: Water level {water_level} is too low \
(min 10)")
    elif sunlight_hours > 12:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} is too \
low (max 12)")
    elif sunlight_hours < 2:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} is too \
high (min 2)")
    else:
        return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    """
    tests all the error
    """
    print("=== Garden Plant Health Checker ===")
    print("\nTesting good values...")
    try:
        print(check_plant_health("tomato", 2, 7))
    except ValueError as ve:
        print(ve)
    print("\nTesting empty plant name...")
    try:
        print(check_plant_health("", 2, 5))
    except ValueError as ve:
        print(ve)
    print("\nTesting bad water level...")
    try:
        print(check_plant_health("tomato", 15, 9))
    except ValueError as ve:
        print(ve)
    print("\nTesting bad sunlight hours...")
    try:
        print(check_plant_health("tomato", 2, 0))
    except ValueError as ve:
        print(ve)
    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
