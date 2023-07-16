class CaseException(Exception):

  def __init__(self, message = None):
    self.message = "[ERROR] BOARD: Cannot generate the game board"
    if message:
        self.message = f"[ERROR] BOARD: {message}\n{self.message}"
    super().__init__(self.message)
  