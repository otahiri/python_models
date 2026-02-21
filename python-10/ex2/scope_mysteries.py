from typing import Any


def mage_counter() -> callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> callable:
    power = initial_power

    def accumulartor(increase: int):
        nonlocal power
        power += increase
        return power
    return accumulartor


def enchantment_factory(enchantment_type: str) -> callable:
    def enchanter(item: str):
        return " ".join([enchantment_type, item])
    return enchanter


def memory_vault() -> dict[str, callable]:
    vault = dict()

    def store(key: str, value: Any) -> None:
        vault[key] = value

    def recall(key: str) -> Any:
        try:
            return vault[key]
        except KeyError:
            return "Memory not found"
    return {'store': store, 'recall': recall}


def main():
    print("\nTesting mage counter...")
    count = mage_counter()
    print(f"Call 1: {count()}")
    print(f"Call 2: {count()}")
    print(f"Call 3: {count()}")
    print("\nTesting enchantment factory...")
    enchant = enchantment_factory("Flaming")
    print(enchant("Sword"))
    enchant = enchantment_factory("Frozen")
    print(enchant("Shield"))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
