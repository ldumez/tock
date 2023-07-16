from pawn.pawnexceptions import PawnException

class Pawn:
    def __init__(self, id) -> None:
        self.id = id
        self.isInGame = False
        self.isLocked = False