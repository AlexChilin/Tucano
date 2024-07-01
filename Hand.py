from Card import *

class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        return ' '.join(str(card) for card in self.cards)

    #def __repr__(self):
        #cards = []
        #for i in self.cards:
            #cards.append(i.value)
        #return str(cards)

    def add_cards(self, cards):
        for card in cards:
            self.cards.append(cards)

    def score(self):
        pointes = 0
        for card in self.cards:
            pointes += card.point
        return pointes

    def save(self):
        return json.dumps({'cards': [card.save() for card in self.cards]})

    @classmethod
    def load(cls, data):
        data = json.loads(data)
        cards = [Card.load(card_data) for card_data in data['cards']]
        hand = cls()
        hand.add_cards(cards)
        return hand

    
