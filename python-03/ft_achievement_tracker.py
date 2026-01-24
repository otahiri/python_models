def create_achievments(*args) -> set:
    return set(args)


def main():
    print("=== Achievement Tracker System ===\n")
    alice = create_achievments('first_kill', 'level_10', 'treasure_hunter',
                               'speed_demon')
    bob = create_achievments('first_kill', 'level_10', 'boss_slayer',
                             'collector')
    charlie = create_achievments('level_10', 'treasure_hunter', 'boss_slayer',
                                 'speed_demon', 'perfectionist')
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")
    print("\n=== Achievement Analytics ===")
    total = alice.union(bob, charlie)
    common = alice.intersection(bob, charlie)
    rare = bob.difference(charlie)
    alice_bob = alice & bob
    unique_alice = alice - (bob | charlie)
    print(f"All unique achievements: {total}")
    print(f"Total unique achievements: {len(total)}")
    print(f"\nCommon to all players: {common}")
    print(f"Rare achievements (1 player): {rare}")
    print(f"Alice vs Bob common: {alice_bob}")
    print(f"Alice unique: {unique_alice}")


if __name__ == "__main__":
    main()
