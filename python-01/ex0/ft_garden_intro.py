def ft_garden_intro(name: str, height: int, age: int):
    """
    print intro to the garden
    name: the name of the plant
    height: the height of the plant
    age: the age of the plant
    """
    print("=== Welcome to My Garden ===")
    print("Plant:", name)
    print("Height:", height, "cm")
    print("Age:", age, "days")


if __name__ == "__main__":
    ft_garden_intro("rose", 25, 30)
