from pawn.pawn import Pawn
from pawn.pawnexceptions import PawnException

class Player:

  def __init__(self, name, color):
    self.name = name
    self.color = color
    self.deck = None
    self.pawns = []
  
  def addPawn(self, pawn):
    if type(pawn) == Pawn:
      self.pawns.append(pawn)
    else:
      raise PawnException('This is not a pawn')
  
  def addDeck(self, deck):
    self.deck = deck
    
  def __str__(self):
    return f"{self.name} is {self.color.name}"
