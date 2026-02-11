from typing import Dict
from ex2 import Magical, Combatable, Card


class EliteCard (Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        health = {"common": 5, "rare": 10, "legendary": 15, "mythic": 20}
        super().__init__(name, cost, rarity)
        self.health = health[self.rarity]

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
        mana_cost = {"common": 1, "rare": 2, "legendary": 3, "mythic": 4}
        res: Dict = dict()
        res["caster"] = self.name
        res["spell"] = spell_name
        res["targets"] = targets
        res["mana_used"] = mana_cost[self.rarity]
        return res

    def defend(self, incoming_damage: int) -> dict:
        defense = {"common": 1, "rare": 2, "legendary": 3, "mythic": 4}
        res: Dict = dict()
        self.health -= incoming_damage - defense[self.rarity]
        res["defender"] = self.name
        res["damage_taken"] = incoming_damage - defense[self.rarity]
        res["damage_blocked"] = defense[self.rarity]
        res["still_alive"] = self.health > 0
        return res

    def get_combat_stats(self) -> dict:
        defense = {"common": 1, "rare": 2, "legendary": 3, "mythic": 4}
        res: Dict = dict()
        res["fighter"] = self.name
        res["attack"] = self.attack
        res["defense"] = defense[self.rarity]
        return res

    def channel_mana(self, amount: int) -> dict:
        res: Dict = dict()
        res["channeled"] = amount
        res["total_mana"] = self.cost - amount
        res["total_mana"] = 0 if res["total_mana"] > 0 else res["total_mana"]
        return res

    def get_magic_stats(self) -> dict:
        defense = {"common": 1, "rare": 2, "legendary": 3, "mythic": 4}
        res: Dict = dict()
        res["name"] = self.name
        res["cost"] = self.cost
        res["magic_defense"] = defense[self.rarity]
        return res
