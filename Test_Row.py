import unittest
from Card import Card
from Row import Row
import json


class TestRow(unittest.TestCase):
    def setUp(self):
        self.row = Row()
        self.card1 = Card('pineapple')
        self.card2 = Card('coconut')
        self.row.add_card(self.card1)
        self.row.add_card(self.card2)

    def test_add_card(self):
        self.assertEqual(len(self.row.cards), 2)

    def test_take_cards(self):
        taken_cards = self.row.take_cards()
        self.assertEqual(len(taken_cards), 2)
        self.assertEqual(taken_cards[0].kind, 'pineapple')
        self.assertEqual(taken_cards[1].kind, 'coconut')
        self.assertEqual(len(self.row.cards), 0)

    def test_save(self):
        expected_json = json.dumps({'cards': [self.card1.save(), self.card2.save()]})
        self.assertEqual(self.row.save(), expected_json)

    def test_load(self):
        json_data = json.dumps({'cards': [self.card1.save(), self.card2.save()]})
        loaded_row = Row.load(json_data)
        self.assertEqual(len(loaded_row.cards), 2)
        self.assertEqual(loaded_row.cards[0].kind, 'pineapple')
        self.assertEqual(loaded_row.cards[1].kind, 'coconut')


if __name__ == '__main__':
    unittest.main()#Работает!

