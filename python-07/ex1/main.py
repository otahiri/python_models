from ex1 import Deck, SpellCard, ArtifactCard, CreatureCard


def main() -> None:
    deck = Deck()
    print("\n=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")
    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 5, 10)
    lightning = SpellCard("Lightning Bolt", 3, "Legendary", "Damage")
    mana_crystal = ArtifactCard("Mana Crystal", 2, "Common", 3, "Buff", )
    deck.add_card(dragon)
    deck.add_card(lightning)
    deck.add_card(mana_crystal)
    print(f"Deck stats: {deck.get_deck_stats()}")


if __name__ == "__main__":
    main()
