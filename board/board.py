from board.boardexceptions import BoardException, BoardSizeError, EndPointsPositionError, StartPointsPositionError
from json import load as jload
from board.case import Case, CaseBasic, CaseEnd, CaseStand, CaseStart
from board.caseexceptions import CaseException
from team.team import Team
#+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
#| 1 | 2 | 3 | 4 | 5 |X6 | 7 | 8 | 9 | 10| 11| 12| 13| 14| 15| 16| 17| 18|
#+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
#| 68|       | 1 |                                                   | 19|
#+---+       +---+                                                   +---+
#| 67|       | 2 |                                                   | 20|
#+---+       +---+                                   +---+---+---+---+---+
#| 66|       | 3 |                                   | 4 | 3 | 2 | 1 | 21|
#+---+       +---+                                   +---+---+---+---+---+
#| 65|       | 4 |                                                   | 22|
#+---+       +---+                                                   +---+
#| 64|                                                               |X23|
#+---+                                                               +---+
#| 63|                                                               | 24|
#+---+                                                               +---+
#| 62|                                                               | 25|
#+---+                                                               +---+
#| 61|                                                               | 26|
#+---+                                                               +---+
#| 60|                                                               | 27|
#+---+                                                               +---+
#| 59|                                                               | 28|
#+---+                                                               +---+
#| 58|                                                               | 29|
#+---+                                                               +---+
#|X57|                                                               | 30|
#+---+                                                   +---+       +---+
#| 56|                                                   | 4 |       | 31|
#+---+---+---+---+---+                                   +---+       +---+
#| 55| 1 | 2 | 3 | 4 |                                   | 3 |       | 32|
#+---+---+---+---+---+                                   +---+       +---+
#| 54|                                                   | 2 |       | 33|
#+---+                                                   +---+       +---+
#| 53|                                                   | 1 |       | 34|
#+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
#| 52| 51| 50| 49| 48| 47| 46| 45| 44| 43| 42| 41|X40| 39| 38| 37| 36| 35|
#+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+

class Board:
  def __init__(self, configuration):
    #get configuration
    try:     
        self.board_configuration = configuration['board_configuration']
        self.board_size = self.board_configuration['size']
        self.end_points_position = self.board_configuration['end_points_position']
        self.start_points_position = self.board_configuration['start_points_position']
        
        self.global_configuration = configuration['global_configuration']
        self.nb_players = self.global_configuration['number_of_players']
        self.number_of_pawns_by_players = self.global_configuration['number_of_pawns_by_players']
    except Exception as e:
        raise BoardException(f"Bad JSON. ({e})")    

    try:
      self.sizeIsConsistant()
      self.side_size = self.computeSideSize()
      self.end_points = self.configureEndPointsPosition()
      self.start_points = self.configureStartPointsPosition()
      
    except BoardSizeError as err:
      print(err)
      raise Exception("Cannot generate the game board.")

    except EndPointsPositionError as err:
      print(err)
      raise Exception("Cannot generate the game board.")

    except StartPointsPositionError as err:
      print(err)

    try:
      self.board_cases = self.createBoardCases()
      self.stand_cases = self.createStandCases()
    except CaseException as err:
      print(err)
      
      
  #the board is a square
  def sizeIsConsistant(self):
    if self.board_size % self.nb_players == 0:
      return True
    raise BoardSizeError(self.nb_players)

  def computeSideSize(self):
    return int(self.board_size / self.nb_players)

  def configureEndPointsPosition(self):
    if self.end_points_position < 2 or self.end_points_position > self.side_size:
      raise EndPointsPositionError(2, self.side_size, self.end_points_position)

    positions = []
    for p in range(self.nb_players):
      c_position = p * self.side_size + self.end_points_position
      positions.append(int(c_position))
    return positions

  def configureStartPointsPosition(self):
    if self.start_points_position <= self.end_points_position or self.start_points_position > self.side_size:
      raise StartPointsPositionError(self.end_points_position + 1, self.side_size, self.start_points_position)

    positions = []
    for p in range(self.nb_players):
      c_position = p * self.side_size + self.start_points_position
      positions.append(int(c_position))
    return positions
  
  def createBoardCases(self):
    cases = []
    index=0
    for c_i in range(self.board_size):
      if c_i in self.end_points:
        cases.append(CaseEnd(c_i))
      elif c_i in self.start_points:
        cases.append(CaseStart(c_i))
      else:
        cases.append(CaseBasic(c_i))
    return cases   

  def createStandCases(self):
    stand_cases = []
    for p_i in range(self.nb_players):
      cases = []
      for c_i in range(self.number_of_pawns_by_players):
        cases.append(CaseStand(id=c_i,player_id=p_i))
      stand_cases.append(cases)
    return stand_cases

  def configureTeamsAndPlayers(self, teams:Team):
    t_i = 0
    for team in teams:
      p_i = t_i
      for player in team.players:
        self.board_cases[self.end_points[p_i]].addPlayer(player)
        self.board_cases[self.start_points[p_i]].addPlayer(player)
        p_i += team.nb_players
      t_i += 1
    pass

  def calcuateSideAngles(self):
    self.side_angle = 180 - (360 / self.nb_players)

  def __str__(self):
    return f"\n\
=====================================\n\n\
[INFO] BOARD: \n\n\
\tboard_size = {self.board_size}\n\
\tnb_players = {self.nb_players}\n\
\tend_points_position = {self.end_points_position}\n\
\tstart_points_position = {self.start_points_position}\n\
\tside_size = {self.side_size}\n\
\tend_points = {self.end_points}\n\
\tstart_points = {self.start_points}\n\n\
=====================================\n\
"
  

