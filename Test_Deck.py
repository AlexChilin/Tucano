import unittest
from Card import Card
from Deck import Deck


class TestCard(unittest.TestCase):

    def setUp(self):
        self.card = Card('pineapple')

    def test_score_valid(self):
        self.assertEqual(self.card.score('pineapple', 2), 6)

    def test_score_invalid_kind(self):
        with self.assertRaises(ValueError):
            self.card.score('invalid_kind', 2)

    def test_save_load(self):
        card_json = self.card.save()
        loaded_card = Card.load(card_json)
        self.assertEqual(loaded_card.kind, 'pineapple')


class TestDeck(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()
        self.deck.cards = [Card(kind) for kind in ['pineapple', 'coconut', 'fig']]

    def test_draw_card(self):
        card = self.deck.draw_card()
        self.assertEqual(card.kind, 'fig')
        self.assertEqual(self.deck.remaining_cards(), 2)

    def test_shuffle(self):
        original_cards = [card.kind for card in self.deck.cards]
        self.deck.shuffle()
        shuffled_cards = [card.kind for card in self.deck.cards]
        self.assertNotEqual(original_cards, shuffled_cards)

    def test_save_load(self):
        deck_json = self.deck.save()
        loaded_deck = Deck.load(deck_json)
        self.assertEqual(loaded_deck.remaining_cards(), 3)
        self.assertEqual([card.kind for card in loaded_deck.cards], ['pineapple', 'coconut', 'fig'])


if __name__ == '__main__':
    unittest.main()
