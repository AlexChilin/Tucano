from Card import Card


class Hand:
    def __init__(self, cards=None):
        if cards is None:
            cards = []
        self.cards = cards

    def __str__(self):
        return ', '.join(map(str, self.cards))

    def __repr__(self):
        return ' '.join(map(str, self.cards))

    def add_cards(self, cards: list[Card]):
        for c in cards:
            self.cards.append(c)

    def score(self, hands: list['Hand'] = None):
        card_counts = self.get_dictionary()
        s = 0
        for k, v in card_counts.items():
            leader = False
            if k in Card.SPETSCARDS:
                if hands is not None:
                    counts = [list(map(str, hand.cards)).count(k) for hand in hands]
                    leader = (max(counts) == v)
            s += Card.score(k, v, leader)
        return s

    def get_dictionary(self):
        card_counts = dict()
        for c in self.cards:
            card = c.kind
            if card not in card_counts:
                card_counts[card] = 0
            card_counts[card] += 1
        return card_counts

    def save(self):
        return [c.save() for c in self.cards]

    @classmethod
    def load(cls, data):
        cards = [Card.load(card) for card in data]
        return Hand(cards)
