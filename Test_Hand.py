import unittest
from Hand import Hand
from Card import Card


    def test_add_cards(self):
        hand = Hand()
        card1 = Card('fig', 'lime')
        card2 = Card('lime', 'pineapple')

        hand.add_cards([card1, card2])

        self.assertEqual(len(hand.cards), 2)
        self.assertIn(card1, hand.cards)
        self.assertIn(card2, hand.cards)

    def test_score(self):
        hand = Hand()
        card1 = Card('rambutan', 'acai berry')
        card2 = Card('orange', 'banana')

        hand.add_cards([card1, card2])

        self.assertEqual(hand.score(), 17)


if __name__ == '__main__':
    unittest.main()
