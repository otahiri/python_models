from alchemy.grimoire import spellbook, validate_ingredients


def main() -> None:
    print("\n=== Circular Curse Breaking ===\n")
    print("Testing ingredient validation:")
    print("validate_ingredients(\"fire air\"): "
          + validate_ingredients("fire air"))
    print("validate_ingredients(\"dragon scales\"): "
          + validate_ingredients("dragon scales"))


if __name__ == "__main__":
    main()
