from typing import Dict, List
from ex4 import TournamentCard


class TournamentPlatform:
    def __init__(self) -> None:
        self.deck: List = list()
        self.matches = 0

    def register_card(self, card: TournamentCard) -> str:
        try:
            if not isinstance(card, TournamentCard):
                raise ValueError
            self.deck.append(card)
        except ValueError:
            print("invalid card")
            exit(1)
        return f"card with id {card.id} registered successfully"

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        res: Dict = dict()
        card1: TournamentCard = next(card for card in self.deck
                                     if card.id == card1_id)
        card2: TournamentCard = next(card for card in self.deck
                                     if card.id == card2_id)
        if not card1 or not card2:
            print("invalid card detected")
            exit(1)
        if card1.calculate_rating() <= card2.calculate_rating():
            winner = card2
            loser = card1
        else:
            winner = card1
            loser = card2
        winner.wins += 1
        loser.loses += 1
        res["winner"] = winner.id
        res["loser"] = loser.id
        res["winner_rating"] = winner.calculate_rating()
        res["loser_rating"] = loser.calculate_rating()
        self.matches += 1
        return res

    def get_leaderboard(self) -> list:
        sorted_list = sorted(self.deck, key=lambda a: a.calculate_rating())
        res = []
        rank = 1
        for card in sorted_list:
            res.append(f"{rank}. {card.name} - Rating: \
{card.calculate_rating()} ({card.wins}-{card.loses})")
            rank += 1

        return res

    def generate_tournament_report(self) -> dict:
        res: Dict = dict()
        res["total_cards"] = len(self.deck)
        res["matches_played"] = self.matches
        res["avg_rating"] = sum([card.calculate_rating() for card in
                                self.deck]) // len(self.deck)
        res["platform_status"] = "active" if res["matches_played"]\
            else "inactive"
        return res
