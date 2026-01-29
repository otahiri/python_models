def create_cords(x: int, y: int, z: int) -> tuple:
    """
    create a tuple of coordinates

    :param x: x coordinates
    :param y: y coordinates
    :param z: z coordinates
    :return: tuple representing the point in a 3d space
    """
    position = tuple([x, y, z])
    return position


def parse_cords(cords: str) -> tuple:
    """
    parse coordinates from a string given by the user

    :param cords: the string containing the coordinates
    :return: tuple containing the coordinates x, y and z
    """
    position = ()
    try:
        position = tuple([int(x) for x in cords.split(",")])
    except ValueError:
        print("Error parsing coordinates: invalid literal for \
int() with base 10: 'abc'")
        print("Error details - Type: ValueError, Args: (\"invalid literal for \
int() with base 10: 'abc'\",)")
    if position:
        print(f"Parsed position: {position}")
    return position


def print_cords(position: tuple) -> None:
    """
    print the coordinates

    :param position: tuple containing the coordinates
    """
    print(f"Player at x={position[0]}, y={position[1]}, z={position[2]}")
    print(f"Coordinates: X={position[0]}, Y={position[1]}, Z={position[2]}")


def count_distance(start: tuple, end: tuple) -> float:
    """
    count the euclidean distance

    :param start: start point
    :param end: end point
    :return: distance from start to end
    """
    distance = 0
    try:
        distance = ((end[0] - start[0]) ** 2 +
                    (end[1] - start[1]) ** 2 +
                    (end[2] - start[2]) ** 2) ** 0.5
    except ValueError:
        print("Error parsing coordinates: invalid literal for \
int() with base 10: 'abc'")
        print("Error details - Type: ValueError, Args: (\"invalid literal for \
int() with base 10: 'abc'\",)")
        return 0
    print(f"Distance between {start} and {end}: \
{distance: .2f} ft_achievement_tracker.py")
    return distance


def main() -> None:
    """
    main program function
    """
    start = (0, 0, 0)
    print("=== Game Coordinate System ===")
    position = create_cords(10, 20, 5)
    print(f"\nPosition created: {position}")
    count_distance(start, position)
    position_str = "3,4,0"
    print(f"\nParsing coordinates: \"{position_str}\"")
    position = parse_cords(position_str)
    count_distance(start, position)
    invalid_cords = "abc,def,ghi"
    print(f"\nParsing invalid coordinates: \"{invalid_cords}\"")
    invalid_position = parse_cords(invalid_cords)
    invalid_position = invalid_position
    print("\nUnpacking demonstration:")
    print_cords(position)


if __name__ == "__main__":
    main()
