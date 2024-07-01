import json
from random import shuffle

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


class Card:
    KINDS: ['pineapple', 'coconut', 'fig', 'orange', 'rambutan', 'pomegranate',
            'lime', 'avocado', 'carambola', 'acai berry', 'papaya', 'lychee', 'banana']
    CARD_COUNTS: {'pineapple': 3, 'coconut': 6, 'fig': 4, 'orange': 4, 'rambutan': 5,
                  'carambola': 5, 'pomegranate': 6, 'avocado': 5, 'lime': 2, 'acai berry': 6,
                  'papaya': 4, 'lychee': 2, 'banana': 5}
    CARD_BONUS = {'pineapple': (0, -2, -4), 'coconut': (8, 6, 4, 2, 0, -2), 'fig': (-2, 0, 9, 16),'orange': (4 , 8, 12, 0),
                  'rambutan': (3, 6, 9, 12 ,15), 'lime': (-2, -8), 'avocado': (3, 6, 9, 12 ,15), 'carambola': (1, 3, 6, 10, 15),
                  'acai berry': (1, 2, 3, 5, 8, 13), 'lychee': (5, 12), banana: (2 ,4 , 6, 8, 10)} #и так далее

    def __init__(self, kind):
        if kind not in self.KINDS:
            raise ValueError(f"Invalid card kind: {kind}")
        self.kind = kind

    def __str__(self):
        return f"Card(kind={self.kind})"

    def score(self, kind, multiplier):
        if kind not in self.KINDS:
            raise ValueError(f"Invalid card kind: {kind}")
        return self.CARD_COUNTS[kind] * multiplier

    def save(self):
        return json.dumps({'kind': self.kind})

    @staticmethod
    def load(json_str):
        data = json.loads(json_str)
        return Card(data['kind'])


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
        for i in self.cards:
            pointes += i.point
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


class Row:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        if card is not None:
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


class GameState:
    def __init__(self, players, rows, deck):
        self.players = players
        self.current_player = 0
        self.rows = rows
        self.deck = deck

    def add_cards(self):
        for _ in range(3):
            row = Row()
            for _ in range(19):
                row.add_card(self.deck.draw_card())
            self.rows.append(row)

    def take_row(self, player, row):
        cards = self.rows[row].take_cards()
        self.players[player].hand.add_cards(cards)

    def save(self):
        with open('savefile.json', 'w', encoding = 'utf-8') as f:
        json.dumps({
            'players': [player.save() for player in self.players],
            'current_player': self.current_player,
            'rows': [row.save() for row in self.rows],
            'deck': self.deck.save()
        })

    @classmethod
    def load(cls, data):
        data = json.loads(data)
        players = [Player.load(player_data) for player_data in data['players']]
        rows = [Row.load(row_data) for row_data in data['rows']]
        deck = Deck.load(data['deck'])
        state = cls(players, rows, deck)
        state.current_player = data['current_player']
        return state


class Human(Player):
    def choose_row(self, rows, players):
        pass


class AI(Player):
    def choose_row(self, rows, players):
        pass


class GameInteractions:
    def __init__(self):
        self.game_state = None

    def run(self):
        self.game_state = self.load()
        self.request_players()
        self.game_state.add_cards()

        while len(self.game_state.rows) > 1:
            self.print_rows()
            self.print_player()

            current_player = self.game_state.players[self.game_state.current_player]
            row = current_player.choose_row(self.game_state.rows, self.game_state.players)
            self.game_state.take_row(self.game_state.current_player, row)
            self.game_state.current_player = (self.game_state.current_player + 1) % len(self.game_state.players)

    def load(self):
        pass

    def request_players(self):
        pass

    def print_rows(self):
        pass

    def print_player(self):
        pass

print('ok')
