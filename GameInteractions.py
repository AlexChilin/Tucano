from GameState import *
from Row import *

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

    @staticmethod
    def print_rows(rows):
        for _ in range(3):
            print(f'{_ + 1}- колода: {rows[_]}')

    @staticmethod
    def print_player_results(game_state):
        for player in game_state.players:
            print(f'{player} - {player.hand.score()}')
            if player.hand.score() > res:
                res = player.hand.score()
        print(f'{player} (набрал {res} очков)')
        print(f'that a grande vittoria')
