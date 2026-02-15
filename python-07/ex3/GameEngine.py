from typing import Dict
from ex3 import CardFactory, GameStrategy
from ex1 import Deck
from ex1 import CreatureCard


class GameEngine:
    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy
        self.deck = Deck()
        self.enemy = Deck()

    def simulate_turn(self) -> dict:
        res: Dict = dict()
        res["cards_played"] = [card.name for card in self.deck.deck]
        res["mana_used"] = sum([card.cost for card in self.deck.deck])
        res["targets_attacked"] = [card.name for card in self.enemy.deck]
        res["damage_dealt"] = sum([card.attack for card in self.deck.deck
                                   if isinstance(card, CreatureCard)])
        return res

    def get_engine_status(self) -> dict:
        res: Dict = dict()
        res["Factory"] = self.factory.__class__.__name__
        res["Strategy"] = self.strategy.get_strategy_name()
        types: Dict = {"Creature": [], "Spell": [], "Artifact": []}
        for card in self.deck.deck:
            types[card.type].append(card.name)
        res["Available types"] = types
        return res
