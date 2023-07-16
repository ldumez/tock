class DeckException(Exception):

  def __init__(self, message = None):
    self.message = "[ERROR] DECK: Fail to start the game."
    if message:
        self.message = f"[ERROR] DECK: {message}\n{self.message}"
    super().__init__(self.message)