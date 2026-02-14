from ex4 import Rankable
from ex0 import Card
from ex2 import Combatable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str, id: str) -> None:
        super().__init__(name, cost, rarity)
        self.id = id


    def play(self, game_state: dict) -> dict:
        ...

    def attack(self, target) -> dict:
        ...

    def calculate_rating(self) -> int:
        ...

    def get_tournament_stats(self) -> dict:
        ...
