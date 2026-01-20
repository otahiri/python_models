import alchemy
from alchemy.potions import strength_potion
from alchemy.potions import healing_potion as heal
from alchemy.elements import create_fire, create_water


def first_method():
    print("\nMethod 1 - Full module import:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")


def second_method():
    print("\nMethod 2 - Specific function import:")
    print(f"create_water(): {create_water()}")


def third_method():
    print("\nMethod 3 - Aliased import:")
    print(f"heal(): {heal()}")


def fourth_method():
    print("\nMethod 4 - Multiple imports:")
    print(f"create_earth(): {alchemy.elements.create_earth()}")
    print(f"create_fire(): {create_fire()}")
    print(f"strength_potion(): {strength_potion()}")


if __name__ == "__main__":
    print("\n=== Import Transmutation Mastery ===")
    first_method()
    second_method()
    third_method()
    fourth_method()
    print("\nAll import transmutation methods mastered!")
