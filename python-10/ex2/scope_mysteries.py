def mage_counter() -> callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> callable:
    pass


def enchantment_factory(enchantment_type: str) -> callable:
    pass


def memory_vault() -> dict[str, callable]:
    pass


def main():
    count = mage_counter()
    print(count)
    count = mage_counter()
    print(count)
    count = mage_counter()
    print(count)


main()
