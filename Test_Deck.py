from Deck import Deck
from Card import Card

def test_deck():
    deck = Deck()
    card1 = Card()
    card2 = Card()
    deck.cards = []

    assert deck.remaining_cards() == 2

    deck.shuffle()
    assert deck.remaining_cards() == 2

    drawn_card = deck.draw_card()
    assert drawn_card == card2
    assert deck.remaining_cards() == 1

    saved_deck = deck.save()
    new_deck = Deck.load(saved_deck)
    assert new_deck.remaining_cards() == deck.remaining_cards()
