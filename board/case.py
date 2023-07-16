from board.casetype import CaseType

class Case:
    def __init__(self, id, color='#c9c9c9', case_type=CaseType.BASIC) -> None:
        self.color = color
        self.type = case_type
        self.id = id
        self.pawn_on = None
        self.next_cases = []
    
    def movePlayerPawnOn(self, pawn):
        self.pawn_on = pawn

class CaseBasic(Case):
    def __init__(self, id) -> None:
        super().__init__(id, '#c9c9c9', CaseType.BASIC)

class CasePlayer(Case):
    def __init__(self, id, color, case_type, player=None, private=False, block=False) -> None:
        super().__init__(id, color, case_type)
        self.player = player
        self.private = private
        self.block = block

    def addPlayer(self, player):
        self.player = player

class CaseStart(CasePlayer):
    def __init__(self, id, player = None) -> None:
        super().__init__(id, '#ff3838', CaseType.START, block=True)

class CaseEnd(CasePlayer):
    def __init__(self, id, player = None) -> None:
        super().__init__(id, '#38acff', CaseType.END)

class CaseStand(CasePlayer):
    def __init__(self, id, player_id, player = None) -> None:
        super().__init__(id, '#de38ff', CaseType.STAND, private=True, block=True)
        self.player_id = player_id

class CaseEndStand(CaseStand):
    def __init__(self, id, player_id, player = None) -> None:
        super().__init__(id, '#de38OO', CaseType.ENDSTAND, private=True, block=True)
        self

class CasStartdStand(CaseStand):
    def __init__(self, id, player_id, player = None) -> None:
        super().__init__(id, '#de3855', CaseType.STARTSTAND, private=True, block=True)
        self.player_id = player_id