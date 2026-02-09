from typing import Dict
from ex0 import Card, Types


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int) -> None:
        if not all([isinstance(name, str), isinstance(cost, int),
                    isinstance(rarity, str), isinstance(attack, int),
                    isinstance(health, int)]):
            print("Invalid attribute")
            exit(1)
        super().__init__(name, cost, rarity)
        self.type = Types.CREATURE.value
        self.set_attack(attack)
        self.set_health(health)

    def set_health(self, health: int) -> None:
        if health < 0:
            print("negative health rejected")
            self.health = 0
        else:
            self.health = health

    def set_attack(self, attack: int) -> None:
        if attack < 0:
            print("negative attack rejected")
            self.attack = 0
        else:
            self.attack = attack

    def play(self, game_state: dict) -> dict:
        res: Dict = dict()
        try:
            mana_left = game_state["mana"]
            playable = super().is_playable(mana_left)
            if playable:
                res["card_played"] = self.name
                res["mana_used"] = self.cost
                res["effect"] = "Creature summoned to \
battlefield"
                return res
        except (KeyError, ValueError, TypeError):
            print("Invalid game state")
            exit(1)
        return res

    def attack_target(self, target) -> dict:
        res: Dict = dict()
        try:
            res["attacker"] = self.name
            res["target"] = target.name
            res["damage_dealt"] = self.attack
            res["combat_resolved"] = self.attack >= target.health
        except ValueError:
            print("Invalid target")
        return res
