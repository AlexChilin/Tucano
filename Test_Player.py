import unittest
from player import Player
from hand import Hand

class TestPlayer(unittest.TestCase):

    def test_init(self):
        hand = Hand([])
        player = Player('Alice', hand)
        self.assertEqual(player.name, 'Alice')
        self.assertEqual(player.hand, hand)

    def test_repr(self):
        hand = Hand([Card('A')])
        player = Player('Bob', hand)
        self.assertEqual(repr(player), "Bob: A ")

    def test_choose_row(self):
        hand = Hand([Card('2')])
        player = Player('Charlie', hand)
        rows = {'row1': [Card('3')], 'row2': [Card('4')]}
        players = [Player('Dave', hand)]
        self.assertIsNone(player.choose_row(rows, players))

    def test_save_load(self):
        hand = Hand([Card('5')])
        player = Player('Eve', hand)
        player_json = player.save()
        loaded_player = Player.load(player_json)
        self.assertEqual(loaded_player.name, 'Eve')
        self.assertEqual(loaded_player.hand.cards[0].value, '5')

if __name__ == '__main__':
    unittest.main()
