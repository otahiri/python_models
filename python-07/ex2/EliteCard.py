from typing import Dict
from ex2 import Magical, Combatable, Card


class EliteCard (Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        super().__init__(name, cost, rarity)

    def play(self, game_state: dict) -> dict:
        res: Dict = dict()
        try:
            if super().is_playable(game_state["mana"]):
                res["card_played"] = self.name
                res["mana_used"] = self.cost
                res["effect"] = "Creature summoned to \
battlefield"
        except (KeyError, ValueError, TypeError):
            print("Invalid game state")
            exit(1)
        return res

    def attack(self, target) -> dict:
        res: Dict = dict()
        res["attacker"] = self.name
        res["target"] = target
        res["damage"] = self.attack
        res["combat_type"] = "melee"
        return res

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        pass

    def guard(self, damage: int) -> Dict:
        defense = {"common": 1, "rare": 2, "legendary": 3, "mythic": 4}
        res: Dict = dict()
        self.health -= damage - defense[self.rarity]
        res["defender"] = self.name
        res["damage_taken"] = damage - defense[self.rarity]
        res["damage_blocked"] = defense[self.rarity]
        res["still_alive"] = self.health > 0
        return res
