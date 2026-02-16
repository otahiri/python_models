from enum import Enum
from ex0 import Card, Types
from ex0.CreatureCard import CreatureCard
from typing import Dict


class Effect(Enum):
    MYTHIC = 4
    LEGENDARY = 3
    RARE = 2
    COMMON = 1


def get_message(power: int, effect_type: str) -> str:
    if effect_type.lower() == "heal":
        return f"healed target by {power}"
    elif effect_type.lower() == "damage":
        return f"Deal {power} damage to target"
    elif effect_type.lower() in ["buff", "debuff"]:
        return f"{effect_type} applied to target for {power} turns"
    else:
        print("Invalid effect")
        exit(1)


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.type = Types.SPELL.value
        self.effect_type = effect_type
        self.power = 0
        for member in Effect:
            if member.name.lower() == rarity.lower():
                self.power = member.value
        if not self.power:
            print("Invalid rarity")
            exit(1)

    def play(self, game_state: dict) -> dict:
        res: Dict = dict()
        try:
            mana_left = game_state["mana"]
            playable = super().is_playable(mana_left)
            if playable:
                res["card_played"] = self.name
                res["mana_used"] = self.cost
                res["effect"] = get_message(self.power,
                                            self.effect_type)
                return res
        except (KeyError, ValueError, TypeError):
            print("Invalid game state")
            exit(1)
        return res

    def resolve_effect(self, targets: list) -> dict:
        res:  Dict = dict()
        for target in targets:
            if not isinstance(target, CreatureCard):
                print("Invalid target found")
                exit(1)
            res[target.name] = target.name + \
                get_message(self.power, self.effect_type)
            if self.effect_type == "heal":
                target.health += self.power
            elif self.effect_type == "damage":
                target.health -= self.power
        return res
