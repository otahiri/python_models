from ex2 import EliteCard
from ex1 import CreatureCard
import inspect


def main() -> None:
    arcane_warrior = EliteCard("Arcane Warrior", 10, "mythic")
    enemy = CreatureCard("Enemy", 3, "rare", 3, 10)
    enemy_one = CreatureCard("Enemy1", 3, "rare", 3, 10)
    enemy_two = CreatureCard("Enemy2", 3, "rare", 3, 10)
    bases = arcane_warrior.__class__.__bases__
    classes = dict()
    for base in bases:
        classes[base.__name__] = [x[0] for x in
                                  inspect.getmembers(base, lambda a:
                                                     inspect.isfunction(a))
                                  if not x[0].startswith("__")]
    print("\n=== DataDeck Ability System ===\n")
    print(f"{arcane_warrior.__class__.__name__} capabilities:")
    for key, value in classes.items():
        print(f" - {key}: {value}")
    print(f"\nPlaying {arcane_warrior.name} (Elite Card):\n")
    print("Combat phase:")
    print(f"Attack result: {arcane_warrior.attack(enemy)}")
    print(f" Defense result: {arcane_warrior.defend(5)}")
    print("Magic phase:")
    print(f"Spell cast: \
{arcane_warrior.cast_spell('Fireball', [enemy_one, enemy_two])}")
    print(f"Mana channel: {arcane_warrior.channel_mana(3)}")
    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
