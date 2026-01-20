import alchemy


def direct_modules_test() -> None:
    print("\nTesting direct module access:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
    print(f"alchemy.elements.create_water(): \
{alchemy.elements.create_water()}")
    print(f"alchemy.elements.create_earth(): \
{alchemy.elements.create_earth()}")
    print(f"alchemy.elements.create_air(): {alchemy.elements.create_air()}")


def package_level_test() -> None:
    print("\nTesting package-level access (controlled by __init__.py):")
    print(f"alchemy.create_fire(): {alchemy.create_fire()}")
    print(f"alchemy.create_water(): {alchemy.create_water()}")
    try:
        print(alchemy.create_earth())
    except AttributeError:
        print("alchemy.create_earth(): AttributeError - not exposed")
    try:
        print(alchemy.create_air())
    except AttributeError:
        print("alchemy.create_air(): AttributeError - not exposed")


if __name__ == "__main__":
    print("\n=== Sacred Scroll Mastery ===")
    direct_modules_test()
    package_level_test()
    with open("alchemy/__init__.py") as fd:
        string = fd.read()
        lines = string.splitlines()
        print("\n" + lines[3], "\n" + lines[4])
