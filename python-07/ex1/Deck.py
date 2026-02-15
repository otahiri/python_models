from typing import Dict, List
import math
import random
from ex0 import Card


class Deck:
    def __init__(self) -> None:
        self.deck: List = []

    def add_card(self, card: Card) -> None:
        try:
            if not isinstance(card, Card):
                raise AttributeError
            self.deck.append(card)
        except (AttributeError):
            print("Invalid card")
            exit(1)

    def remove_card(self, card_name: str) -> bool:
        if not isinstance(card_name, str):
            print("Invalid card")
            exit(1)
        for card in self.deck:
            if card.name == card_name:
                self.deck.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.deck)

    def draw_card(self) -> Card:
        try:
            card = self.deck[0]
            print(f"\nDrew: {card.name} ({card.type})")
            return card
        except IndexError:
            print("empty deck")
            exit(1)

    def get_deck_stats(self) -> dict:
        res: Dict = dict()
        res['total_cards'] = len(self.deck)
        res['creatures'] = len([x for x in self.deck if x.type == "Creature"])
        res['spells'] = len([x for x in self.deck if x.type == "Spell"])
        res['artifacts'] = len([x for x in self.deck if x.type == "Artifact"])
        res['avg_cost'] = float(math.ceil(sum([x.cost for x in self.deck])
                                / len(self.deck)))
        return res
