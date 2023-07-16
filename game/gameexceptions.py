class GameException(Exception):

  def __init__(self, message = None):
    self.message = "[ERROR] GAME: Fail to start the game."
    if message:
        self.message = f"[ERROR] GAME: {message}\n{self.message}"
    super().__init__(self.message)

class GameConfigurationError(GameException):
  
  def __init__(self, field_name = "Unknown"):
    self.message = f"Bad game configuration ({field_name})."
    super().__init__(self.message)

class GameConfigurationFileError(GameException):
  
  def __init__(self):
    self.message = "Bad game configuration file."
    super().__init__(self.message)