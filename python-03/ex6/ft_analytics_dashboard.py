from typing_extensions import TypeForm


def comprehence_list(player_names: list, player_scores: list) -> None:
    print("=== List Comprehension Examples ===")
    print(f"High scorers (>2000): \
{[score for  score in player_scores if score > 2000]}")
    print(f"Scores doubled: {[score * 2 for score in player_scores]}")
    print(f"Active players: {player_names}")


def dic_comprehention(player_scores: dict, player_achieve: dict):
    all_scores = dict()
    score_rank = {"high": 0, "medium": 0, "low": 0}
    achieve_count = dict()

    print("\n=== Dict Comprehension Examples ===")
    for key, value in player_scores.items():
        all_scores[key] = value
        if value < 1900:
            score_rank["low"] += 1
        elif 1900 < value < 2100:
            score_rank["medium"] += 1
        elif value > 2100:
            score_rank["high"] += 1
    for key, value in player_achieve.items():
        achieve_count[key] = len(value)
    print(f"Player scores: {all_scores}")
    print(f"Score categories: {score_rank}")
    print(f"Achievement counts: {achieve_count}")


def set_comprehention(player_list: set, achievements: list):
    total = []
    for s in achievements:
        total.extend(s)
    count = dict()
    for x in total:
        count[x] = count.get(x, 0) + 1
    unique = set()
    for key, value in count.items():
        if value == 1:
            unique.add(key)

    print("\n=== Set Comprehension Examples ===")
    print(f"Unique players: {player_list}")
    print(f"Unique achievements: {unique}")
    print(f"Active regions: {'north', 'east', 'central'}")


def combined_analysis(player_achieve: dict, player_scores: dict):
    print("\n=== Combined Analysis ===")
    total_unique = set()
    total_score = 0
    max_score = list(player_scores.keys())[0]
    for value in player_achieve.values():
        total_unique.update(value)
    for key, value in player_scores.items():
        total_score += value
        max_score = key if value > player_scores[max_score] else max_score
    print(f"Total players: {len(player_scores.values())}")
    print(f"Total unique achievements: {total_unique}")
    print(f"Average score: {total_score / len(player_scores.values())}")
    print(f"Top performer: {max_score} ({player_scores[max_score]}, \
{len(player_achieve[max_score])} achievements)")


def main() -> None:
    player_scores = {"charlie": 2150, "bob": 1800, "alice": 2300,
                     "diana": 2050}
    player_achieve = {"charlie": {"level_10", "treasure_hunter",
                                  "boss_slayer", "speed_demon",
                                  "perfectionist"},
                      "bob": {"first_kill", "level_10",
                              "boss_slayer", "collector"},
                      "alice": {"first_kill", "level_10",
                                "treasure_hunter", "speed_demon"},
                      "diana": {"first_kill", "level_10",
                                "treasure_hunter", "speed_demon"}}

    print("=== Game Analytics Dashboard ===\n")
    comprehence_list(list(player_scores.keys()),
                     [value for value in player_scores.values()])
    dic_comprehention(player_scores, player_achieve)
    set_comprehention(set(player_achieve.keys()),
                      list(player_achieve.values()))
    combined_analysis(player_achieve, player_scores)


if __name__ == "__main__":
    try:
        main()
    except (ValueError, TypeError):
        print("Warning: invalid data")
