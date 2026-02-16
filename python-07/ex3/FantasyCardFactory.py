import random
import inspect
from typing import Dict
from ex3 import CardFactory
from ex1 import CreatureCard, ArtifactCard, SpellCard
from ex0 import Card


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power:
            card = CreatureCard(str(name_or_power), 5, "Rare", 3, 10)
            return card
        else:
            card = CreatureCard("Enemy Player", 3, "Common", 3, 5)
            return card

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power:
            spell = SpellCard(str(name_or_power), 5, "Rare", "damage")
        else:
            spell = SpellCard("Spell", 3, "Common", "dealt damage to target")
        return spell

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power:
            artifact = ArtifactCard(str(name_or_power), 3, "Rare", 2,
                                    "buff applied to the player")
        else:
            artifact = ArtifactCard("Artifact", 3, "Common", 2,
                                    "buff applied to the player")
        return artifact

    def create_themed_deck(self, size: int) -> dict:
        create: list = [self.create_creature, self.create_spell,
                        self.create_artifact]
        deck: Dict = dict()
        for _ in range(size):
            create_func = random.choice(create)
            card = create_func()
            deck[card.name] = card
        return deck

    def get_supported_types(self) -> dict:
        funcs = [func[0].split("_")[1] for func in
                 inspect.getmembers(self.__class__,
                                    lambda f: inspect.isfunction(f))
                 if len(func[0].split("_")) == 2]
        res: Dict = dict()
        res["types"] = funcs
        res["count"] = len(funcs)
        return res
