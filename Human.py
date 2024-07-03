from Row import Row
from Player import Player


class Human:
    @staticmethod
    def choose_row(self, player: Player, rows: list[Row]):
        while True:
            row = input(f'{player.name}, выберите любую колоду (1 =< n =< 3): ')
            try:
                row = int(row)
            except ValueError:
                row = 0
            if 1 <= row <= 3 and rows[row - 1].cards:
                break
        row -= 1
        player.hand.add_cards(rows[row].take_cards())
        return row
