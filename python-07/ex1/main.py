from ex1 import Deck, SpellCard, ArtifactCard, CreatureCard


def main() -> None:
    deck = Deck()
    game_state = {"mana": 10, "my_turn": True, }
    print("\n=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")
    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 5, 10)
    lightning = SpellCard("Lightning Bolt", 3, "Legendary", "damage")
    mana_crystal = ArtifactCard("Mana Crystal", 2, "Common", 3, "buff", )
    deck.add_card(lightning)
    deck.add_card(mana_crystal)
    deck.add_card(dragon)
    print(f"Deck stats: {deck.get_deck_stats()}")
    print("\nDrawing and playing cards:")
    for _ in range(3):
        card = deck.draw_card()
        print(f"Play result: {card.play(game_state)}")
        deck.remove_card(card.name)
    print("\nPolymorphism in action: Same interface, different card \
behaviors!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
