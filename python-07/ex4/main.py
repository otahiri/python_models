from ex4 import TournamentCard, TournamentPlatform


def main() -> None:
    print("\n=== DataDeck Tournament Platform ===\n")
    print("Registering Tournament Cards...")
    tournament = TournamentPlatform()
    dragon = TournamentCard("Fire Dragon", 9, "legendary", "dragon_001")
    wizard = TournamentCard("Ice Wizard ", 9, "super_rare", "wizard_001")
    tournament.deck.append(dragon)
    tournament.deck.append(wizard)
    for card in tournament.deck:
        res = card.get_tournament_stats()
        keys = list(res.keys())
        print(f"\n{keys[0]} {res[keys[0]]}")
        for key in keys[1:]:
            print(f"{key}: {res[key]}")
    print("\nCreating tournament match...")
    print("Match result:", end="")
    print(tournament.create_match("dragon_001", "wizard_001"))
    print("\nTournament Leaderboard: ")
    for line in tournament.get_leaderboard():
        print(line)
    print("\nPlatform Report:")
    print(tournament.generate_tournament_report())
    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
