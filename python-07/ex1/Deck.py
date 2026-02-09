from typing import Dict, List
import random
from ex0 import Card


class Deck:
    def __init__(self) -> None:
        self.deck: List = []

    def add_card(self, card: Card) -> None:
        self.deck.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.deck:
            if card.name == card_name:
                self.deck.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.deck)

    def draw_card(self) -> Card:
        return self.deck[0]

    def get_deck_stats(self) -> dict:
        res: Dict = dict()
        res['total_cards'] = len(self.deck)
        res['creatures'] = len([x for x in self.deck if x.type == 'creature'])
        res['spells'] = len([x for x in self.deck if x.type == 'spell'])
        res['artifacts'] = len([x for x in self.deck if x.type == 'artifact'])
        res['avg_cost'] = sum([x.cost for x in self.deck]) / len(self.deck)
        return res
