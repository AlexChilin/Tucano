import unittest
from row import row
from card import card

class TestRow(unittest.TestCase):

    def setUp(self):
        self.test_row = row()

    def test_add_card(self):
        test_card = (name='card')
        self.test_row.add_card(test_card)

        self.assertIn(test_card, self.test_row.cards)

    def test_take_cards(self):
        test_card = MagicMock(name='card')
        self.test_row.add_card(test_card)

        cards = self.test_row.take_cards()

        self.assertEqual(cards, [test_card])
        self.assertEqual(self.test_row.cards, [])

    def test_save_and_load(self):
        test_card = card('Test Name', 'Test Type')
        self.test_row.add_card(test_card)

        saved_data = self.test_row.save()
        loaded_row = row.load(saved_data)

        self.assertEqual(len(loaded_row.cards), 1)
        self.assertEqual(loaded_row.cards[0].name, 'Test Name')
        self.assertEqual(loaded_row.cards[0].type, 'Test Type')

if __name__ == '__main__':
    unittest.main()
