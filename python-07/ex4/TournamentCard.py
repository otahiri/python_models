from typing import Dict
from enum import Enum
from ex4 import Rankable
from ex0 import Card
from ex2 import Combatable


class Attack(Enum):
    COMMON = 1
    RARE = 2
    SUPER_RARE = 3
    LEGENDARY = 4
    MYTHIC = 5


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str, id: str) -> None:
        super().__init__(name, cost, rarity)
        self.id = id
        self.atk = Attack.__getitem__(self.rarity.upper()).value
        self.loses = 0
        self.wins = 0

    def play(self, game_state: dict) -> dict:
        res: Dict = dict()
        if not self.is_playable(game_state["mana"]):
            res["is_playable"] = False
        else:
            res["card played"] = self.name
            res["cost"] = self.cost
            res["effect"] = f"{self.name} was summoned to the battlefield"
        return res

    def attack(self, target) -> dict:
        res: Dict = dict()
        if not isinstance(target, Card):
            print("invalid target")
            exit(1)
        res["attacker"] = self.name
        res["target"] = target.name
        res["attack"] = self.atk
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

    def calculate_rating(self) -> int:
        return 1000 + (self.atk * 50)

    def get_tournament_stats(self) -> dict:
        res: Dict = self.get_rank_info()
        res["Record"] = (self.wins, self.loses)
        return res

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.loses += losses

    def get_rank_info(self) -> dict:
        res: Dict = dict()
        res[self.name] = f"(ID: {self.id})"
        res["Interfaces"] = [base.__name__ for base in
                             self.__class__.__bases__]
        res["Rating"] = self.calculate_rating()
        return res
