from ex0 import Card, Types
from typing import Dict


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, durability: int,
                 effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect
        self.active = False
        self.type = Types.ARTIFACT.value

    def play(self, game_state: dict) -> dict:
        res: Dict = dict()
        try:
            mana_left = game_state["mana"]
            playable = super().is_playable(mana_left)
            print(f"Playable: {playable}")
            if playable:
                res["card_played"] = self.name
                res["mana_used"] = self.cost
                res["effect"] = self.effect
                return res
        except (KeyError, ValueError):
            print("Invalid game state")
        return res

    def activate_ability(self) -> dict:
        res: Dict = dict()
        effect = self.effect.split()
        res["duration"] = effect[0][:-1]
        res["value"] = effect[1]
        res["effect"] = effect[2]
        return res
