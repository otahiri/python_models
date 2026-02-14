from typing import Dict
from ex3 import FantasyCardFactory, GameEngine, AggressiveStrategy
from ex1 import CreatureCard, SpellCard


def main() -> None:
    print("\n=== DataDeck Game Engine ===\n")
    print("Configuring Fantasy Card Game...")
    factory = FantasyCardFactory()
    game = GameEngine()
    turns = 0
    agressive = AggressiveStrategy()
    game.configure_engine(factory, agressive)
    game.deck.add_card(game.factory.create_creature("dragon"))
    game.deck.add_card(game.factory.create_creature("goblin"))
    game.deck.add_card(game.factory.create_spell("fireball"))
    game.deck.add_card(game.factory.create_artifact("mana_ring"))
    game_status = game.get_engine_status()
    for key, value in game_status.items():
        print(f"{key}: {value}")
    print("\nSimulating aggressive turn...")
    game.deck.remove_card("mana_ring")
    game.deck.remove_card("fireball")
    game.deck.remove_card("dragon")
    game.deck.remove_card("goblin")
    game.deck.add_card(CreatureCard("Goblin Warrior", 2, "mythic", 8, 10))
    game.deck.add_card(SpellCard("Lightning Bolt", 3, "legendary", "damage"))
    game.deck.add_card(CreatureCard("Fire Dragon", 5, "rare", 5, 10))
    hand = [f"{card.name} ({card.cost})" for card in game.deck.deck]
    print(f"Hand: [{', '.join(hand)}]")
    game.enemy.add_card(game.factory.create_creature())
    print("\nTurn execution:")
    print(f"Strategy: {game.strategy.get_strategy_name()}")
    action = game.strategy.execute_turn([game.deck.deck[0],
                                         game.deck.deck[1]], game.enemy.deck)
    turns += 1
    print("Actions", action)
    print("\nGame Report:")
    report: Dict = {"turns_simulated": turns,
                    "strategy_used": game.strategy.get_strategy_name(),
                    "total_damage": action["damage_dealt"],
                    "cards_created": len(game.deck.deck)}
    print(report)
    print("\nAbstract Factory + Strategy Pattern: \
Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
