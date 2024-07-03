from Card import Card
import json


class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)

    def __repr__(self):
        return ' '.join(str(card) for card in self.cards)

    def add_cards(self, cards):
        for _ in cards:
            self.cards.append(cards)

    def get_dictionary(self):
        card_counts = dict()
        for c in self.cards:
            card_counts[c] += 1
            return card_counts

    def score(self):
        card_counts = self.get_dictionary()
        points = 0
        for c, m in card_counts.items():
            points += Card.score(c, m)
        return points

    def save(self):
        return json.dumps({'cards': [card.save() for card in self.cards]})

    @classmethod
    def load(cls, data):
        data = json.loads(data)
        cards = [Card.load(card_data) for card_data in data['cards']]
        hand = cls()
        hand.add_cards(cards)
        return hand


    
