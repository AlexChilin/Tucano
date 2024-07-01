from random import shuffle
import json
from Card import *


class Deck:
    def __init__(self):
        self.cards = []

    def draw_card(self):
        return self.cards.pop()

    def shuffle(self):
        shuffle(self.cards)

    def remaining_cards(self):
        return len(self.cards)

    def save(self):
        return json.dumps({'cards': [card.save() for card in self.cards]})

    @classmethod
    def load(cls, data):
        data = json.loads(data)
        deck = cls()
        deck.cards = [Card.load(card_data) for card_data in data['cards']]
        return deck
