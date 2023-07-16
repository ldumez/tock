from enum import Enum, auto

class CardValue (Enum):
  AS      = 1
  TWO     = 2
  THREE   = 3
  FOUR    = 4
  FIVE    = 5
  SIX     = 6
  SEVEN   = 7
  HEIGH   = 8
  NINE    = 9
  TEN     = 10
  JACK    = 11
  QUEEN   = 12
  KING    = 13

NUMBER_OF_CARDS_BY_COLOR = len(CardValue)
