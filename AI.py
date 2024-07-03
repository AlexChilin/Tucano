class AI:
  @staticmethod
  def choose_row(rows, player):
    row = random.randint(0, 2)
    player.hand.add_cards(rows[row].take_cards())
    return row
