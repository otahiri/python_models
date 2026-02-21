import operator
import functools
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    if operation == "add":
        return functools.reduce(operator.add, spells)
    elif operation == "multiply":
        return functools.reduce(operator.mul, spells)
    elif operation == "max":
        return functools.reduce(max, spells)
    elif operation == "min":
        return functools.reduce(min, spells)
    else:
        print("invalid operation")
        exit(1)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {"fire_enchant":
            functools.partial(base_enchantment, power=50, element="fire"),
            "ice_enchant":
            functools.partial(base_enchantment, power=50, element="ice"),
            "lightning_enchant":
            functools.partial(base_enchantment, power=50, element="lightning")}


@functools.lru_cache()
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    @functools.singledispatch
    def spell(param: Any):
        return f"{param} was deplyed"

    @spell.register
    def _(param: int):
        return f"spell dealt {param} damage"

    @spell.register
    def _(param: str):
        return f"{param} applied to sword"

    @spell.register
    def _(param: list):
        return f"multi cast skill used {[spell for spell in param]}"
    return spell


def main() -> None:
    print("\nTesting spell reducer...")
    print(f"Sum: {spell_reducer([10, 25, 30, 35], 'add')}")
    print(f"Product: {spell_reducer([240, 1000], 'multiply')}")
    print(f"Max: {spell_reducer([10, 3, 40, 2], 'max')}")
    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
