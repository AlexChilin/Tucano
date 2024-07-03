from Row import Row
from Deck import Deck
from Player import Player
import json


class GameState:
    def __init__(self, players, rows, deck):
        self.players = players
        self.current_player = 0
        self.rows = rows
        self.deck = deck

    def __str__(self):
        player_names = [p.name for p in self.players]
        return f'Игроки: {player_names}'

    def add_cards(self):
        for _ in range(self.rows):
            row = Row()
            for _ in range(len(self.rows)):
                row.add_card(self.deck.draw_card())
            self.rows.append(row)

    def take_row(self, player, row):
        cards = self.rows[row].take_cards()
        self.players[player].hand.add_cards(cards)

    def save(self):
        with open('savefile.json', 'w', encoding='utf-8') as _:
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
