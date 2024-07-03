import unittest
from Card import Card  # Assuming Card class is defined in Card.py
import json


class TestCard(unittest.TestCase):

    def setUp(self):
        self.card = Card('pineapple')  # Example card for testing

    def test_init(self):
        self.assertEqual(self.card.kind, 'pineapple')

    def test_str(self):
        self.assertEqual(str(self.card), "Card(kind=pineapple)")

    #def test_repr(self):
        #self.assertEqual(self.card.repr(), 'pineapple')

    def test_score(self):
        self.assertEqual(self.card.score('pineapple', 2), 6)  # 3 (CARD_COUNTS['pineapple']) * 2

    def test_score_invalid_kind(self):
        with self.assertRaises(ValueError):
            self.card.score('invalid_kind', 2)

    def test_save(self):
        expected_json = json.dumps({'kind': 'pineapple'})
        self.assertEqual(self.card.save(), expected_json)

    def test_load(self):
        card_json = json.dumps({'kind': 'pineapple'})
        loaded_card = Card.load(card_json)
        self.assertEqual(loaded_card.kind, 'pineapple')


if __name__ == '__main__':
    unittest.main()
