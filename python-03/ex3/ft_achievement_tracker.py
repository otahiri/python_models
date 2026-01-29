def main() -> None:
    """
    main program function
    """
    print("=== Achievement Tracker System ===\n")
    alice = set(["first_kill", "level_10", "treasure_hunter",
                "speed_demon"])
    bob = set(["first_kill", "level_10", "boss_slayer",
              "collector"])
    charlie = set(["level_10", "treasure_hunter", "boss_slayer",
                  "speed_demon", "perfectionist"])
    print([f"Player alice achievements: {alice}"])
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")
    print("\n=== Achievement Analytics ===")
    total = alice.union(bob, charlie)
    common = alice.intersection(bob, charlie)
    rare = bob.difference(alice, charlie) | alice.difference(charlie, bob)\
        | charlie.difference(alice, bob)
    alice_bob = alice.intersection(bob)
    unique_alice = alice.difference(bob)
    unique_bob = bob.difference(alice)
    print(f"All unique achievements: {total}")
    print(f"Total unique achievements: {len(total)}")
    print(f"\nCommon to all players: {common}")
    print(f"Rare achievements (1 player): {rare}")
    print()
    print(f"Alice vs Bob common: {alice_bob}")
    print(f"Alice unique: {unique_alice}")
    print(f"Alice unique: {unique_bob}")


if __name__ == "__main__":
    main()
