import json
from Card import *

class Row:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def take_cards(self):
        cards = self.cards.copy()
        self.cards.clear()
        return cards

    def save(self):
        return json.dumps({'cards': [card.save() for card in self.cards]})

    @classmethod
    def load(cls, data):
        data = json.loads(data)
        row = cls()
        row.cards = [Card.load(card_data) for card_data in data['cards']]
        return row
