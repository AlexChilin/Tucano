from Hand import *


class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def __repr__(self):
        cards = ''
        for i in self.hand.cards:
            cards += f'{i.value} '
        return f'{self.name}: {cards}'

    def choose_row(self, rows, players):
        pass

    def save(self):
        return json.dumps({
            'name': self.name,
            'hand': self.hand.save()})

    @classmethod
    def load(cls, data):
        data = json.loads(data)
        hand = Hand.load(data['hand'])
        return cls(data['name'], hand)
