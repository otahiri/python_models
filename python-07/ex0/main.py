from typing import Dict
from ex0.CreatureCard import CreatureCard


def main() -> None:
    game_state: Dict = {"mana": 6, "state": dict()}
    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    print("\n=== DataDeck Card Foundation ===")
    print("\nTesting Abstract Base Class Design:\n")
    print(f"CreatureCard Info: {vars(dragon)}")
    print("\nPlaying Fire Dragon with 6 mana available:")
    print(f"Playable: {dragon.is_playable(game_state["mana"])}")
    res = dragon.play(game_state)
    print(f"Play result: {res}") if res.keys() else None
    print("\nFire Dragon attacks Goblin Warrior:")
    goblin = CreatureCard("Goblin Warrior", 3, "Common", 3, 5)
    print(dragon.attack_target(goblin))
    print("\nTesting insufficient mana (3 available)")
    game_state["mana"] = 3
    res = dragon.play(game_state)
    print(f"Play result: {res}") if res.keys() else None
    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
