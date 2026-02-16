from abc import ABC, abstractmethod
from typing import Tuple
from enum import Enum


class Types(Enum):
    CREATURE = "Creature"
    SPELL = "Spell"
    ARTIFACT = "Artifact"


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        if rarity not in ["Common", "Rare", "Legendary", "Super_rare",
                          "Mythic"]:
            print("invalid rarity detected")
            exit(1)
        self.name = name
        self.cost = cost
        self.rarity = rarity

    def play(self, game_state: dict) -> dict:
        ...
    play = abstractmethod(play)

    def get_card_info(self) -> Tuple:
        return self.name, self.cost, self.rarity

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost
