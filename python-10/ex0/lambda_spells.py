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
    mages = [{'name': 'Rowan', 'power': 95, 'element': 'light'},
             {'name': 'River', 'power': 68, 'element': 'light'},
             {'name': 'Casey', 'power': 58, 'element': 'fire'},
             {'name': 'Storm', 'power': 62, 'element': 'ice'},
             {'name': 'Luna', 'power': 75, 'element': 'light'}]
    spells = ['lightning', 'tsunami', 'earthquake', 'darkness']
    print("\nTesting artifact sorter...")
    print(f"{artifact_sorter(artifacts)}")


if __name__ == "__main__":
    main()
