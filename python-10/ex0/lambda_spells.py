def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a['power'])


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda a: a['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda a: f"* {a} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    return {"max_power": max(mages, key=lambda a: a['power']),
            "min_power": min(mages, key=lambda a: a['power']),
            "avg_power": sum(map(lambda a: a['power'], mages))}


def main() -> None:
    artifacts = [{'name': 'Wind Cloak', 'power': 112, 'type': 'armor'},
                 {'name': 'Water Chalice', 'power': 65, 'type': 'weapon'},
                 {'name': 'Shadow Blade', 'power': 119, 'type': 'relic'},
                 {'name': 'Storm Crown', 'power': 98, 'type': 'weapon'}]
    spells = ['lightning', 'tsunami', 'earthquake', 'darkness']
    print("\nTesting artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    last = sorted_artifacts[-1]
    before_last = sorted_artifacts[-2]
    print(f"{last['name']} ({last['power']}) comes before \
{before_last['name']} ({before_last['power']})")
    print("\nTesting spell transformer...")
    print(" ".join(spell_transformer(spells)))


if __name__ == "__main__":
    try:
        main()
    except IndexError as e:
        print(e)
    except (ValueError, KeyError, TypeError) as e:
        print(e)
