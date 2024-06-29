class Row:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def take_cards(self):
        cards = self.cards
        self.cards = []
        return cards

    def save(self):
        return json.dumps([{"suit": card.suit, "rank": card.rank} for card in self.cards])

    def load(self, data):
        self.cards = [Card(card_data["suit"], card_data["rank"]) for card_data in json.loads(data)]
