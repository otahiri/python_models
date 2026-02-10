import alchemy.elements
from alchemy.elements import create_water
from alchemy.potions import healing_potion as heal, strength_potion
from alchemy.elements import create_fire, create_earth


def first_method() -> None:
    print("\nMethod 1 - Full module import:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")


def second_method() -> None:
    print("\nMethod 2 - Specific function import:")
    print(f"create_water(): {create_water()}")


def third_method() -> None:
    print("\nMethod 3 - Aliased import:")
    print(f"heal(): {heal()}")


def fourth_method() -> None:
    print("\nMethod 4 - Multiple imports:")
    print(f"create_earth(): {create_earth()}")
    print(f"create_fire(): {create_fire()}")
    print(f"strength_potion(): {strength_potion()}")


if __name__ == "__main__":
    print("\n=== Import Transmutation Mastery ===")
    first_method()
    second_method()
    third_method()
    fourth_method()
    print("\nAll import transmutation methods mastered!")
