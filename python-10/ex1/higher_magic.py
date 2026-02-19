def spell_combiner(spell1: callable, spell2: callable) -> callable:
    return lambda *args, **kwargs: (spell1(*args, **kwargs),
                                    spell2(*args, **kwargs))


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    return lambda *args, **kwargs: base_spell(*args, **kwargs) * multiplier


def conditional_caster(condition: callable, spell: callable) -> callable:
    return lambda *args, **kwargs: \
        spell(*args, **kwargs) if condition(*args, **kwargs) \
        else "Spell fizzled"


def spell_sequence(spells: list[callable]) -> callable:
    return lambda *args, **kwargs: [spell(*args, **kwargs) for spell in spells]


def fireball() -> str:
    return "Fireball hits Dragon"


def heal() -> str:
    return "Heals Dragon"


def power(original: int) -> int:
    return original


def main() -> None:
    print("Testing spell combiner...")
    print(f"Combined spell result: {spell_combiner(fireball, heal)()}")
    print("\nTesting power amplifier...")
    amplifier = 3
    print(f"Original: {power(10)}, Amplified: \
{power_amplifier(power, amplifier)(10)}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
