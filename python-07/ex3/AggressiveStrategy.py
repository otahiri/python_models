from typing import Dict
from ex0 import Card
from ex3 import GameStrategy
from ex1 import CreatureCard


class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        atk = {"common": 1, "rare": 2, "legendary": 3, "mythic": 5}
        targets = self.prioritize_targets(battlefield)
        res: Dict = dict()
        res["cards_played"] = [card.name for card in hand
                               if isinstance(card, Card)]
        res["mana_used"] = sum([card.cost for card in hand if
                                isinstance(card, Card)])
        res["targets_attacked"] = [card.name for card in targets]
        res["damage_dealt"] = sum(atk[card.rarity] for card in hand
                                  if isinstance(card, Card)) * len(targets)
        return res

    def get_strategy_name(self) -> str:
        return self.__class__.__name__

    def prioritize_targets(self, available_targets: list) -> list:
        try:
            res = [target for target in available_targets if
                   isinstance(target, CreatureCard)]
        except ValueError:
            print("Warning invalid card detected")
            exit(1)
        return res
