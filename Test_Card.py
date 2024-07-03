import unittest
from Card import Card

def test_score(self):
    test_card = Card('pineapple')
    self.assertEqual(test_card.score('pineapple', 2), 6)
    self.assertEqual(test_card.score('coconut', 3), 18)
    self.assertEqual(test_card.score('fig', 4), 16)
    self.assertEqual(test_card.score('banana', 1), 5)
    with self.assertRaises(ValueError):
        test_card.score('apple', 2)

def test_save_load(self):
    test_card = Card('lime')
    saved_card = test_card.save()
    loaded_card = card.load(saved_card)
    self.assertEqual(test_card.kind, loaded_card.kind)

def test_invalid_kind(self):
    with self.assertRaises(ValueError):
        test_card = Card('mango')


if __name__ == '__main__':
    unittest.main()
