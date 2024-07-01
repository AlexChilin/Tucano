from Deck import *
from Card import *

def test_deck():
    deck = Deck()
    card1 = Card('Hearts', 'A')
    card2 = Card('Diamonds', '10')
    deck.cards = [card1, card2]

    assert deck.remaining_cards() == 2

    deck.shuffle()
    assert deck.remaining_cards() == 2

    drawn_card = deck.draw_card()
    assert drawn_card == card2
    assert deck.remaining_cards() == 1

    saved_deck = deck.save()
    new_deck = Deck.load(saved_deck)
    assert new_deck.remaining_cards() == deck.remaining_cards()
