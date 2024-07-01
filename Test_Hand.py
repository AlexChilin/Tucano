import unittest
from Hand import Hand
from Card import Card

class TestHand(unittest.TestCase):

    def test_add_cards(self):
        hand = Hand()
        card1 = Card('A', 'Hearts')
        card2 = Card('10', 'Spades')

        hand.add_cards([card1, card2])

        self.assertEqual(len(hand.cards), 2)
        self.assertIn(card1, hand.cards)
        self.assertIn(card2, hand.cards)

    def test_score(self):
        hand = Hand()
        card1 = Card('7', 'Diamonds')
        card2 = Card('K', 'Clubs')

        hand.add_cards([card1, card2])

        self.assertEqual(hand.score(), 17)

if __name__ == '__main__':
    unittest.main()
