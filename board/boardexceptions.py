class BoardException(Exception):

  def __init__(self, message = None):
    self.message = "[ERROR] BOARD: Cannot generate the game board"
    if message:
        self.message = f"[ERROR] BOARD: {message}\n{self.message}"
    super().__init__(self.message)
    

class BoardSizeError(BoardException):

  def __init__(self, board_size):
    self.board_size = board_size
    self.message = f"The board size must be a multiple of {self.board_size}"
    super().__init__(self.message)


class EndPointsPositionError(BoardException):

  def __init__(self, min, max, end_points_position):
    self.end_points_position = end_points_position
    self.message = f"The end points position must be between {min} and {max} ({self.end_points_position})"
    super().__init__(self.message)


class StartPointsPositionError(BoardException):

  def __init__(self, min, max, start_points_position):
    self.start_points_position = start_points_position
    self.message = f"The start points position must be between {min} and {max} ({self.start_points_position})"
    super().__init__(self.message)
