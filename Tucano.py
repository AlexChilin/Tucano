import json
import random
from random import shuffle


class Card:
    KINDS = ['pineapple', 'coconut', 'fig', 'orange', 'rambutan', 'pomegranate',
             'lime', 'avocado', 'carambola', 'acai berry', 'papaya', 'lychee', 'banana']
    CARD_COUNTS = {'pineapple': 3, 'coconut': 6, 'fig': 4, 'orange': 4, 'rambutan': 5,
                   'carambola': 5, 'pomegranate': 6, 'avocado': 5, 'lime': 2, 'acai berry': 6,
                   'papaya': 4, 'lychee': 2, 'banana': 5}
    CARD_BONUS = {'pineapple': (0, -2, -4), 'coconut': (8, 6, 4, 2, 0, -2), 'fig': (-2, 0, 9, 16),
                  'orange': (4, 8, 12, 0), 'rambutan': (3, 6, 9, 12, 15), 'lime': (-2, -8),
                  'carambola': (1, 3, 6, 10, 15), 'acai berry': (1, 2, 3, 5, 8, 13), 'lychee': (5, 12)}

    SPETSCARDS = {'banana': (0, 2), 'pomegranate': (-1, 1), 'avocado': (1, 3)}

    def __init__(self, kind):
        self.kind = kind

    def __str__(self):
        return f"Card(kind={self.kind})"

    @staticmethod
    def score(kind, multiplier, leader):
        if kind not in Card.KINDS:
            raise ValueError(f"Invalid card kind: {kind}")
        return Card.CARD_COUNTS[kind] * multiplier

    def save(self):
        return json.dumps({'kind': self.kind})

    @staticmethod
    def load(json_str):
        data = json.loads(json_str)
        return Card(data['kind'])


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


class Player:
    def __init__(self, name: str, hand: Hand = None, is_human: bool = False):
        self.name = name
        if hand is None:
            hand = Hand()
        self.hand = hand
        if is_human:
            self.actor = Human()
        else:
            self.actor = AI()

    def __repr__(self):
        return f'name: {self.name},\nhand: {self.hand}'

    def __str__(self):
        return f'{self.name}'

    def choose_row(self, rows, players: list['Player']):
        return self.actor.choose_row(self, rows, players)

    def save(self):
        data = {'name': self.name,
                'hand': self.hand.save(),
                'is_human': isinstance(self.actor, Human)}
        return data

    @classmethod
    def load(cls, data: dict):
        name = data['name']
        hand = Hand.load(data['hand'])
        is_human = data['is_human']
        return Player(name, hand, is_human)


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


class Human:
    @staticmethod
    def choose_row(player, rows=0):
        while 1 > row and row > 3 or not rows[row-1].cards:
            row = input(f'{player.name}, choose any deck (1 =< n =< 3): ')
            try:
                row = int(row)
            except ValueError:
                row -= 1
        player.hand.add_cards(rows[row].take_cards())
        return row


class AI:
    @staticmethod
    def choose_row(player, rows):
        row = random.randint(0, 2)
        print(f'"{player.name}" choose {row + 1} stack')
        player.hand.add_cards(rows[row].take_cards())
        return row


class GameState:
    def __init__(self, players, rows, current_player, deck):
        self.players = players
        self.current_player = current_player
        self.rows = rows
        self.deck = deck

    def __str__(self):
        player_names = [p.name for p in self.players]
        return f'Players: {player_names}'

    def add_cards(self):
        for _ in range(len(self.rows)):
            row = Row()
            for _ in range(len(self.rows)):
                row.add_card(self.deck.draw_card())
            self.rows.append(row)

    def take_row(self, player, row):
        cards = self.rows[row].take_cards()
        self.players[player].hand.add_cards(cards)

    def save(self):
        with open('savefile.json', 'w', encoding='utf-8') as file:
            json.dump({
                'players': [player.save() for player in self.players],
                'current_player': self.current_player,
                'rows': [row.save() for row in self.rows],
                'deck': self.deck.save()
            }, file)

    @classmethod
    def load(cls, data):
        data = json.loads(data)
        players = [Player.load(player_data) for player_data in data['players']]
        rows = [Row.load(row_data) for row_data in data['rows']]
        deck = Deck.load(data['deck'])
        state = cls(players, rows, data['current_player'], deck)
        return state


class GameInteractions:
    MAX_PLAYERS = 4
    COUNT_ROWS = 3
    SAVE_FILE = 'save-file.json'

    @classmethod
    def run(cls):
        exist_last_game = cls.is_exist_last_game()

        gs = GameState([], [])
        if exist_last_game:
            last_gs = GameState.load(cls.SAVE_FILE)
            print(f'Previous game found: {last_gs}')
            ans = input('Enter "yes" to start a new game: ')
            if ans.lower() == 'yes':
                gs = cls.start_new_game()
            else:
                gs = last_gs
                print('Game loaded')
        else:
            gs = cls.start_new_game()

        total_moves = gs.deck.remaining_cards() // (len(gs.players) * cls.COUNT_ROWS)
        for move in range(total_moves):
            print('-------------------------')
            print(f'Move {move + 1}')
            for i in range(len(gs.players)):
                print('Rows:')
                cls.print_rows(gs.rows)
                current_mover = gs.players[gs.current_player]
                current_mover.choose_row(gs.rows, gs.players)

                gs.add_cards()
                gs.current_player = (gs.current_player + 1) % len(gs.players)
                gs.save()

        hands = [p.hand for p in gs.players]
        for p in gs.players:
            print(f'Player {p} scored - {p.hand.score(hands)} points')

        max_score = 0
        winner = ''
        for p in gs.players:
            cur_score = p.hand.score(hands)
            if cur_score > max_score:
                winner = p
                max_score = cur_score

        print(f'Winner - {winner}')

    @staticmethod
    def print_rows(rows):
        for j in range(3):
            print(f'{j + 1}: {rows[j]}')

    @classmethod
    def is_exist_last_game(cls):
        try:
            GameState.load(cls.SAVE_FILE)
        except Exception:
            return False
        return True

    @classmethod
    def start_new_game(cls):
        count_players = 0
        while not 1 < count_players <= cls.MAX_PLAYERS:
            count_players = int(input(f'Введите количество игроков (2 =< n =< {cls.MAX_PLAYERS}): '))

        count_humans = -1
        while not 0 <= count_humans <= count_players:
            count_humans = int(input(f'Введите число людей (0 =< n =< {count_players}): '))

        players = []
        for i in range(count_humans):
            name = input(f'Введите имя {i + 1}-го игрока: ')
            players.append(Player(name, None, True))

        for i in range(count_players - count_humans):
            name = 'AI' + str(i)
            players.append(Player(name, None, False))

        current_player = 0
        deck = Deck()
        deck.shuffle()

        rows = []
        for i in range(GameInteractions.COUNT_ROWS):
            rows.append(Row([deck.draw_card()]))
        rows[1].add_card(deck.draw_card())

        return GameState(players, rows, current_player, deck)


if __name__ == 'main':
    GameInteractions.run()
